from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models, IntegrityError
from django.core.validators import EmailValidator
import random


# Create your models here.
class User(AbstractUser):

	def generate_passkey(self, n_length) -> str:
		perm = (str(random.randint(0, 9)) for _ in range(n_length))
		return f"IHEMCNPS-{''.join(perm)}"

	def save(self, *args, **kwargs):
		while True:
			try:
				self.passkey = self.generate_passkey(4)
				super().save(*args, **kwargs)
				break
			except IntegrityError:
				pass

	class Meta:
		unique_together = ['email', 'passkey']

	username = models.CharField(_('Email'), max_length=150, unique=True, validators=[EmailValidator])
	name = models.CharField(max_length=200, null=True, blank=False)
	passkey = models.CharField(max_length=13, unique=True, editable=False)
	is_student = models.BooleanField(default=False)
	is_educator = models.BooleanField(default=False)

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'username'
