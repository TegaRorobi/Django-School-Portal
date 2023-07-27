from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models, IntegrityError
from django.core.validators import EmailValidator, RegexValidator
from django.conf import settings
import random



class User(AbstractUser):

	def generate_passkey(self, const, rand_len) -> str:
		ret = (str(random.randint(0, 9)) for _ in range(rand_len))
		return const + ''.join(ret)

	class Meta:
		unique_together = ['username', 'passkey']

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
	dob = models.DateField(_('Date of Birth'), null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(_('Phone Number'), max_length=14, null=True, validators=[PHONE_NUMBER_VALIDATOR])
	passkey = models.CharField(max_length=13, unique=True, blank=True, editable=False)
	is_student = models.BooleanField()
	is_teacher = models.BooleanField()
	is_admin = models.BooleanField()


	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'username'

	def save(self, *args, **kwargs):
		if self.password and not self.password.startswith('pbkdf2_sha256'):
			self.set_password(self.password)
			# alternatively, 
			# self.password = django.contrib.auth.hashers.make_password(self.password)

		# is_student should be mutually exclusive with other flags
		# is_teacher and is_admin are not mutually exclusive.
		if self.is_student + self.is_teacher + self.is_admin > 1 and self.is_student:
			raise IntegrityError("A user account attached to a student profile cannot be attached to any other profile.")
			
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


	def __str__(self):
		return self.name if self.name else self.username
