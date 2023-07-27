from django.db import models, IntegrityError
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
import datetime

UserModel = get_user_model()


class Subject(models.Model):
	label = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.label



class Grade(models.Model):

	GRADE_LABEL_CHOICES = [
		('Kindergarten 1', 'Kindergarten 1'),
		('Kindergarten 2', 'Kindergarten 2'),
		('Nursery 1', 'Nursery 1'),
		('Nursery 2', 'Nursery 2'),
		('Primary 1', 'Primary 1'),
		('Primary 2', 'Primary 2'),
		('Primary 3', 'Primary 3'),
		('Primary 4', 'Primary 4'),
		('Primary 5', 'Primary 5'),
	]
	label = models.CharField(max_length=15,choices=GRADE_LABEL_CHOICES)
	subjects = models.ManyToManyField(Subject, related_name='grades_taught_in')

	def __str__(self):
		return self.label



class TeacherProfile(models.Model):

	user = models.OneToOneField(UserModel, related_name='teacher_profile', on_delete=models.CASCADE)
	bio = models.TextField(_('Biography'), null=True)
	image = models.ImageField(upload_to='images/teacher_profiles')
	grades = models.ManyToManyField(Grade, related_name='teachers')

	qualifications = models.CharField(max_length=500, null=True)
	subject_specializations = models.ManyToManyField(Subject, related_name='specialized_teachers')

	# timestamps
	date_created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if self.user.is_student:
			# log an error message
			raise IntegrityError("It is illegal to attach a teacher profile to a user object already attached to a student profile")
		self.user.is_teacher = True
		self.user.save()
		super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)



class StudentProfile(models.Model):

	user = models.OneToOneField(UserModel, related_name='student_profile', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/student_profiles')
	grade = models.ForeignKey(Grade, related_name='students', on_delete=models.PROTECT)
	subjects = models.ManyToManyField(Subject, related_name='offering_students')

	# timestamps
	date_created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		try:
			if self.user.teacher_profile:
				# log an error message
				return
		except:
			self.user.is_student = True
			# making sure all selected subjects are offered by the selected grade.
			# O(n) time complexity and O(n) space complexity, where n is the number of
			# subjects offered by the grade which is fairly constant
			hashset = set([subject.label for subject in self.grade.subjects.all()])
			for subject in self.subjects.all():
				if subject.label not in hashset:
					# log an error message
					return
			super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)





class AdminProfile(models.Model):

	user = models.OneToOneField(UserModel, related_name='admin_profile', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/admin_profiles')
	position = models.CharField(max_length=300)
	bio = models.TextField()

	#timestamps
	date_created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	
	def save(self, *args, **kwargs):
		if self.user.is_student:
			# log an error message
			raise IntegrityError("It is illegal to attach an admin profile to a user object already attached to a student profile")
		self.user.is_admin = True
		self.user.save()
		super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)