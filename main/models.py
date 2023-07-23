from django.db import models
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
	image = models.ImageField(upload_to='images/teacher_profiles')
	grades = models.ManyToManyField(Grade, related_name='teachers')

	# timestamps
	date_created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		try:
			if self.user.student_profile:
				# log an error message
				return
		except:
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
			# making sure all selected subjects are offered by the selected grade.
			hashset = set([subject.label for subject in self.grade.subjects.all()])
			for subject in self.subjects.all():
				if subject.label not in hashset:
					# log an error message
					return
			super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)

