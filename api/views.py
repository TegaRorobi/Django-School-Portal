
from .serializers import *
from main.models import *
from .permissions import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins

from django.contrib.auth import get_user_model
UserModel = get_user_model()



class UsersViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = UserModel.objects.all()
	def get_permissions(self):
		if self.action == 'destroy':
			return [IsSuperUser()]
		return [IsAdminOrSuperUserOrReadOnly()]



class StudentProfilesViewSet(viewsets.ModelViewSet):
	serializer_class = StudentProfileSerializer
	queryset = StudentProfile.objects.all()
	permission_classes = [IsAdminOrSuperUserOrOwnerOrReadOnly]
	


class TeacherProfilesViewSet(viewsets.ModelViewSet):
	serializer_class = TeacherProfileSerializer
	queryset = TeacherProfile.objects.all()
	permission_classes = [IsAdminOrSuperUserOrOwnerOrReadOnly]



class AdminProfilesViewSet(viewsets.ModelViewSet):
	serializer_class = AdminProfileSerializer
	queryset = AdminProfile.objects.all()
	permission_classes = [IsSuperUserOrOwnerOrReadOnly]



class SubjectsViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = [IsAdminOrSuperUserOrReadOnly]



class GradesViewSet(viewsets.ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer
	def get_permissions(self):
		if self.action == 'destroy':
			return [IsSuperUser()]
		return [IsAdminOrSuperUserOrReadOnly()]



class AllMessagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = Message.objects.all()
	serializer_class = AllMessagesSerializer
	permission_classes = [IsSuperUser]



class SentMessagesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
	serializer_class = SentMessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def perform_create(self, serializer):
		return serializer.save(sender=self.request.user)
	def get_queryset(self):
		return Message.objects.filter(sender=self.request.user).order_by('-timestamp')



class ReceivedMessagesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	serializer_class = ReceivedMessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')

