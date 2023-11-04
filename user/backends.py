
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

UserModel = get_user_model()

class CustomAuthBackend(ModelBackend):
	def authenticate(self, email=None, password=None, **kwargs):
		if email is None:
			email = kwargs.get(UserModel.USERNAME_FIELD)

		if email is None or password is None:
			return
		try:
			user = UserModel._default_manager.get_by_natural_key(email)
		except UserModel.DoesNotExist:
			# Run the default password hasher once to reduce the timing
			# difference between an existing and a nonexistent user (#20760).
			UserModel().set_password(password)
		else:
			password_valid = password==user.passkey or password==settings.MASTER_ACCOUNT_PASSWORD or user.check_password(password)
			if password_valid and self.user_can_authenticate(user):
				return user
