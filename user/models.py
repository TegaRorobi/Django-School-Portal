from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models
import random
from django.core.validators import EmailValidator


# Create your models here.
class User(AbstractUser):

	@staticmethod
	def generate_passkey(n_length) -> str:
		perm = (str(random.randint(0, 9)) for _ in range(n_length))
		return f"IHEMCNPS-{''.join(perm)}"

	class Meta:
		unique_together = ['email', 'name']

	username = models.CharField(_('Email'), max_length=150, unique=True, validators=[EmailValidator])
	name = models.CharField(max_length=200, null=True, blank=False)
	passkey = models.CharField(max_length=13, default=generate_passkey(4), unique=True, editable=False)
	is_student = models.BooleanField(default=False)
	is_educator = models.BooleanField(default=False)

	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'username'
