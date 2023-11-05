from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class LoginView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'user/login.html')

	def post(self, request, *args, **kwargs):
		email = request.POST.get('username')
		password = request.POST.get('password')

		usr = authenticate(email=email, password=password)
		if usr:
			login(request, usr)
			messages.success(request, f"Successfully logged in as {usr.name}")
		else:
			# log an error message
			messages.error(request, f"CredentialsError: Credentials not authorized!")
			print('user not authenticated')

		return redirect(reverse('main:home'))


class LogoutView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return render(request, 'user/logout.html')