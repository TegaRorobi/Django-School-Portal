from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models, IntegrityError
from django.core.validators import EmailValidator, RegexValidator
import random


class User(AbstractUser):

	def generate_passkey(self, const, rand_len) -> str:
		ret = (str(random.randint(0, 9)) for _ in range(rand_len))
		return const + ''.join(ret)

	def save(self, *args, **kwargs):
		if not self.passkey:
			while True:
				try:
					self.passkey = self.generate_passkey("IHEMCNPS-", 4)
					super().save(*args, **kwargs)
					break
				except IntegrityError:
					pass
		else:
			super().save(*args, **kwargs)


	class Meta:
		unique_together = ['username', 'passkey']

	ACCOUNT_TYPE_CHOICES = [
		("admin", "Admin"),
		("student", "Student"),
		("educator", "Educator")
	]

	GENDER_CHOICES = [
		('m', 'Male'),
		('f', 'Female')
	]

	# Works with Nigeria's country code, but can be modified for any country
	PHONE_NUMBER_VALIDATOR = RegexValidator(
		regex = "\+(234)[789][01]\d{8}",
		message = "Invalid formatting. Here's an example:\n\t'+2348011235813' corresponds to '08011235813'"
	)

	name = models.CharField(_('Full Name'), max_length=200, null=True, blank=False)
	username = models.CharField(_('Email'), max_length=150, unique=True, validators=[EmailValidator])
	gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
	account_type = models.CharField(max_length=8, choices=ACCOUNT_TYPE_CHOICES, null=True)
	dob = models.DateField(_('Date of Birth'), null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(_('Phone Number'), max_length=14, null=True, validators=[PHONE_NUMBER_VALIDATOR])
	passkey = models.CharField(max_length=13, unique=True, blank=True, editable=False)


	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'username'

	def __str__(self):
		return self.name if self.name else self.username
