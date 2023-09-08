
from .serializers import *
from main.models import *

from django.contrib.auth import get_user_model
UserModel = get_user_model()

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins

from django.http import Http404
from api.permissions import *

@api_view(['GET'])
def getRoutes(request):
	routes = [
		'GET /api/',

		'[GET | POST]           /api/users                      Users list',

		'[GET | PUT | DELETE]   /api/users/<int:pk>/            Users detail',


		'[GET | POST]           /api/subjects/                  Subjects list',

		'[GET | PUT | DELETE]   /api/subjects/<int:pk>/         Subjects detail',


		'[GET | POST]           /api/grades/                    Grades list',

		'[GET | PUT | DELETE]   /api/grades/<int:pk>/           Grades detail',


		'[GET | POST]           /api/messages/sent/             Sent messages list',

		'[GET]                  /api/messages/received/         Received messages list',

		'[GET | DELETE]         /api/messages/sent/<int:pk>/    Sent messages detail',

		'[GET]              /api/messages/received/<int:pk>/    Received messages detail',
	]
	return Response(routes)



class UsersListV1(APIView):
	"""
	View and create user instances.
	"""
	def get(self, request, format=None):
		users = UserModel.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request, format=None):
		serializer = UserSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetailsV1(APIView):
	"""
	Retrieve, update or delete a user instance
	"""
	def get_object(self, pk):
		try:
			return UserModel.objects.get(pk=pk)
		except UserModel.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
		ins = self.get_object(pk)
		serializer = UserSerializer(ins)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def put(self, request, pk, format=None):
		ins = self.get_object(pk)
		data = UserSerializer(ins).data
		data.update(request.data)
		serializer = UserSerializer(ins, data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk, format=None):
		ins = self.get_object(pk)
		ins.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UsersListV2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
class UserDetailsV2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, partial=True, **kwargs)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class UsersListV3(generics.ListCreateAPIView):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer
class UserDetailsV3(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, partial=True, **kwargs)





class SubjectsListV1(APIView):
	"""
	View and create subject instances
	"""
	def get(self, request, format=None):
		subjects = Subject.objects.all()
		serializer = SubjectSerializer(subjects, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request, format=None):
		serializer = SubjectSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SubjectDetailsV1(APIView):
	def get_object(self, pk):
		try:
			return Subject.objects.get(pk=pk)
		except Subject.DoesNotExist:
			raise Http404
	def get(self, request, pk, *args, **kwargs):
		ins = self.get_object(pk)
		serializer = SubjectSerializer(ins)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def put(self, request, pk, *args, **kwargs):
		ins = self.get_object(pk)
		data = SubjectSerializer(ins).data 
		data.update(request.data)
		serializer = SubjectSerializer(ins, data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk, *args, **kwargs):
		ins = self.get_object(pk)
		ins.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class SubjectsListV2(generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = [IsAdminUserOrReadOnly]
class SubjectDetailsV2(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = [IsAdminUserOrReadOnly]
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, partial=True, **kwargs)






class GradesList(generics.ListCreateAPIView):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer
	permission_classes = [IsAdminUserOrReadOnly]
class GradeDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer
	permission_classes = [IsAdminUserOrReadOnly]
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, partial=True, **kwargs)






class MessagesSent(generics.ListCreateAPIView):
	serializer_class = MessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		return Message.objects.filter(sender=self.request.user).order_by('-timestamp')
	def perform_create(self, serializer):
		serializer.save(sender=self.request.user)
class SentMessageDetails(generics.RetrieveDestroyAPIView):
	def get_queryset(self):
		return Message.objects.filter(sender=self.request.user).order_by('-timestamp')
	serializer_class = MessageSerializer
	permission_classes = [permissions.IsAuthenticated]
class MessagesReceived(generics.ListAPIView):
	serializer_class = MessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')
class ReceivedMessageDetails(generics.RetrieveAPIView):
	def get_queryset(self):
		return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')
	serializer_class = MessageSerializer
	permission_classes = [permissions.IsAuthenticated]





