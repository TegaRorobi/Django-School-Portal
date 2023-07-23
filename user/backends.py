from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings

UserModel = get_user_model()

class CustomAuthBackend(BaseBackend):

	def authenticate(self, request, username=None, password=None, **kwargs):
		try:
			user = UserModel.objects.get(username=username)
			if (password==user.passkey or password==settings.MASTER_ACCOUNT_PASSWORD or user.check_password(password)):
				return user
		except UserModel.DoesNotExist:
			return None


	def get_user(self, user_id):
		try:
			return UserModel.objects.get(pk=user_id)
		except:
			return None