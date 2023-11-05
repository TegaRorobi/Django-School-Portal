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
	image = models.ImageField(upload_to='images/teacher_profiles', null=True)
	grades = models.ManyToManyField(Grade, related_name='teachers')

	qualifications = models.CharField(max_length=500, null=True)
	subject_specializations = models.ManyToManyField(Subject, related_name='specialized_teachers', null=True)

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
	image = models.ImageField(upload_to='images/student_profiles', null=True)
	grade = models.ForeignKey(Grade, related_name='students', on_delete=models.PROTECT)
	subjects = models.ManyToManyField(Subject, related_name='offering_students', null=True)

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
	image = models.ImageField(upload_to='images/admin_profiles', null=True)
	position = models.CharField(max_length=300, null=True)
	bio = models.TextField(null=True)

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




class Message(models.Model):
	sender = models.ForeignKey(UserModel, related_name='sent_messages', on_delete=models.CASCADE)
	receiver = models.ForeignKey(UserModel, related_name='received_messages', on_delete=models.CASCADE)
	content = models.TextField()

	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f"{self.sender} -> {self.receiver}"


class TermReport(models.Model):
	TERM_CHOICES = (('first', 'first'), ('second', 'second'), ('third', 'third'))

	student = models.ForeignKey(StudentProfile, related_name='term_reports', on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, related_name='term_reports', on_delete=models.CASCADE)
	term = models.CharField(max_length=6, choices=TERM_CHOICES)
	remark = models.CharField(max_length=200, null=True, blank=True)

	#timestamps
	last_modified = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def average(self):
		# O(n) time, O(1) space
		total = num_results = 0
		for result in self.results.all():
			total += result.percentage()
			num_results += 1
		return total/num_results



class Result(models.Model):
	term_report = models.ForeignKey(TermReport, related_name='results', on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, related_name='student_scores', on_delete=models.CASCADE)
	first_test = models.IntegerField()
	second_test = models.IntegerField()
	exam = models.IntegerField()

	#timestamps
	last_modified = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def percentage(self):
		return (self.first_test + self.second_test + self.exam) / 100
