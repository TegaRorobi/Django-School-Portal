from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _
from django.db import models, IntegrityError
from django.core.validators import RegexValidator
import random


class CustomUserManager(UserManager):
	def _create_user(self, username, email, password, **extra_fields):
		if not email:
			raise ValueError("The given username must be set")

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)

		while True:
			try:
				user.passkey = self.model.generate_passkey(None, "IHEMCNPS-", 4)
				user.save(using=self._db)
				break
			except IntegrityError as e:
				pass
		return user

	def create_user(self, username=None, email=None, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", False)
		extra_fields.setdefault("is_superuser", False)

		is_admin = extra_fields.get('is_admin', False)
		is_teacher = extra_fields.get('is_teacher', False)
		is_student = extra_fields.get('is_student', False)

		if is_admin + is_student + is_teacher > 1 and is_student:
			raise IntegrityError("A user account marked as 'student' cannot be attached to any other profile.")
		
		if is_admin + is_student + is_teacher == 0:
			raise IntegrityError("Unknown type for user account, please select one of: 'is_admin', 'is_student', 'is_teacher'")
		
		return self._create_user(username=username, email=email, password=password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		return super().create_superuser(username=None, email=email, password=password, **extra_fields)


class User(AbstractUser):

	def generate_passkey(self, const, rand_len) -> str:
		ret = (str(random.randint(0, 9)) for _ in range(rand_len))
		return const + ''.join(ret)

	class Meta:
		unique_together = ['email', 'passkey']

	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female')
	]

	# Works with Nigeria's country code, but can be modified for any country
	PHONE_NUMBER_VALIDATOR = RegexValidator(
		regex = "\+(234)[789][01]\d{8}",
		message = "Invalid formatting. Here's an example:\n\t'+2348011235813' corresponds to '08011235813'"
	)

	name = models.CharField(_('Full Name'), max_length=200, null=True, blank=False)
	email = models.EmailField(_('Email Address'), unique=True)
	gender = models.CharField(_('Gender'), max_length=1, null=True, choices=GENDER_CHOICES)
	dob = models.DateField(_('Date of Birth'), null=True)
	address = models.CharField(_('House Address'), max_length=200, null=True)
	phone = models.CharField(_('Phone Number'), max_length=14, null=True, validators=[PHONE_NUMBER_VALIDATOR])
	passkey = models.CharField(max_length=13, unique=True, blank=True, editable=False)

	username = None

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.name if self.name else self.email
