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

	username = models.CharField(_('Email'), max_length=150, unique=True, validators=[EmailValidator])
	name = models.CharField(max_length=200, null=True, blank=False)
	passkey = models.CharField(max_length=13, unique=True, blank=True)
	account_type = models.CharField(max_length=8, choices=ACCOUNT_TYPE_CHOICES, null=True)

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'username'
