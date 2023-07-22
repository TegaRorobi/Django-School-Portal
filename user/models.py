from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models, IntegrityError
from django.core.validators import EmailValidator
import random


class User(AbstractUser):

	def generate_passkey(self, const, rand_len) -> str:
		ret = (str(random.randint(0, 9)) for _ in range(rand_len))
		return const + ''.join(ret)

	def save(self, *args, **kwargs):
		while True:
			try:
				self.passkey = self.generate_passkey("IHEMCNPS-", 4)
				super().save(*args, **kwargs)
				break
			except IntegrityError:
				pass

	class Meta:
		unique_together = ['email', 'passkey']

	ACCOUNT_TYPE_CHOICES = [
		("admin", "Admin"),
		("student", "Student"),
		("educator", "Educator")
	]

	GENDER_CHOICES = [
		('m', 'Male'),
		('f', 'Female')
	]

	name = models.CharField(max_length=200, null=True, blank=False)
	username = models.CharField(_('Email'), max_length=150, unique=True, validators=[EmailValidator])
	gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
	account_type = models.CharField(max_length=8, choices=ACCOUNT_TYPE_CHOICES, null=True)
	dob = models.DateField(_('Date of Birth'), null=True)
	passkey = models.CharField(max_length=13, unique=True, blank=True)

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'username'
