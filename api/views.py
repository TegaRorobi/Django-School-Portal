
from .serializers import *
from main.models import *
from .permissions import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins

from django.contrib.auth import get_user_model
UserModel = get_user_model()



class UsersViewSet(viewsets.ModelViewSet):

	"API Viewset to get all users, retrieve the details of a specific user, "\
	"create a new user, update an existing user, as well as delete a user."

	serializer_class = UserSerializer
	queryset = UserModel.objects.prefetch_related('sent_messages', 'received_messages').order_by('-id')

	def get_permissions(self):
		if self.action == 'destroy':
			return [IsSuperUser()]
		return [IsAdminOrSuperUserOrReadOnly()]



class StudentProfilesViewSet(viewsets.ModelViewSet):

	"API Viewset to get all student profiles, retrieve the details of a specific student profile, "\
	"create a new student profile, update an existing student profile and also delete a student profile."

	serializer_class = StudentProfileSerializer
	queryset = StudentProfile.objects.prefetch_related('user', 'subjects').order_by('-id')
	permission_classes = [IsAdminOrSuperUserOrOwnerOrReadOnly]
	


class TeacherProfilesViewSet(viewsets.ModelViewSet):

	"API Viewset to get all teacher profiles, retrieve the details of a specific teacher profile, "\
	"create a new teacher profile, update an existing teacher profile and also delete a teacher profile."

	serializer_class = TeacherProfileSerializer
	queryset = TeacherProfile.objects.prefetch_related('grades', 'user', 'subject_specializations').order_by('-id')
	permission_classes = [IsAdminOrSuperUserOrOwnerOrReadOnly]



class AdminProfilesViewSet(viewsets.ModelViewSet):

	"API Viewset to get all admin profiles, retrieve the details of a specific admin profile, "\
	"create a new admin profile, update an existing admin profile and also delete an admin profile."

	serializer_class = AdminProfileSerializer
	queryset = AdminProfile.objects.prefetch_related('user').order_by('-id')
	permission_classes = [IsSuperUserOrOwnerOrReadOnly]



class SubjectsViewSet(viewsets.ModelViewSet):

	"API Viewset to get all subjects, retrieve a specific subject, create a new subject, "\
	"update an existing one, as well as deleting one."

	queryset = Subject.objects.prefetch_related('grades_taught_in').order_by('label')
	serializer_class = SubjectSerializer
	permission_classes = [IsAdminOrSuperUserOrReadOnly]



class GradesViewSet(viewsets.ModelViewSet):

	"API Viewset to get all grades, retrieve a specific grade's details, "\
	"create a new grade, and also update and delete existing grades."

	queryset = Grade.objects.prefetch_related('subjects', 'students', 'teachers').order_by('label')
	serializer_class = GradeSerializer
	def get_permissions(self):
		if self.action == 'destroy':
			return [IsSuperUser()]
		return [IsAdminOrSuperUserOrReadOnly()]



class AllMessagesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

	"API Viewset to get all messages and retrieve a specific message. "\
	"Note: This viewset may not be applicable in the final application, it may be terminated "\
	"as a superuser being able to view all user messages may have ethical issues."

	queryset = Message.objects.prefetch_related('sender', 'receiver').order_by('-timestamp')
	serializer_class = AllMessagesSerializer
	permission_classes = [IsSuperUser]



class SentMessagesViewSet(viewsets.ModelViewSet):

	"API Viewset to get all sent messages of a particular user (the currently authenticated user), "\
	"retrieve specific messages, send new messages to other people, as well as update and delete them."

	serializer_class = SentMessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def perform_create(self, serializer):
		return serializer.save(sender=self.request.user)
	def get_queryset(self):
		return Message.objects.prefetch_related('receiver').filter(sender=self.request.user).order_by('-timestamp')



class ReceivedMessagesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

	"API Vievset to perform read operations on received messages, i.e getting all received messages, "\
	"retrieving the detail of a specific received message."
	
	serializer_class = ReceivedMessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		return Message.objects.prefetch_related('sender').filter(receiver=self.request.user).order_by('-timestamp')


class TermViewSet(
	mixins.ListModelMixin, mixins.CreateModelMixin, 
	mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
	viewsets.GenericViewSet):
	queryset = Term.objects.all().order_by('-start_date')
	serializer_class = TermSerializer
	permission_classes = [IsSuperUserOrReadOnly]