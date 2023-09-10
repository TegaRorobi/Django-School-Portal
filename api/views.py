
from .serializers import *
from main.models import *
from .permissions import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins


@api_view(['GET'])
def getRoutes(request):
	routes = [
		'GET /api/',

		'[GET | POST]           /api/users                      Users list',

		'[GET | PUT | DELETE]   /api/users/<int:pk>/            User detail',


		'[GET | POST]           /api/subjects/                  Subjects list',

		'[GET | PUT | DELETE]   /api/subjects/<int:pk>/         Subject detail',


		'[GET | POST]           /api/grades/                    Grades list',

		'[GET | PUT | DELETE]   /api/grades/<int:pk>/           Grade detail',


		'[GET | POST]           /api/messages/sent/             Sent messages list',

		'[GET]                  /api/messages/received/         Received messages list',

		'[GET | DELETE]         /api/messages/sent/<int:pk>/    Sent messages detail',

		'[GET]              /api/messages/received/<int:pk>/    Received messages detail',
	]
	return Response(routes)

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

