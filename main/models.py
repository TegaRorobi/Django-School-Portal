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

