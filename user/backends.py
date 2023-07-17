from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(BaseBackend):

	def authenticate(self, request, username=None, password=None, **kwargs):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.get(username=username)
			if user.check_password(password) or user.passkey == password:
				return user
		except UserModel.DoesNotExist:
			return None



	def get_user(self, user_id):
		UserModel = get_user_model()
		try:
			return UserModel.objects.get(pk=user_id)
		except:
			return None