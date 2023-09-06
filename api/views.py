
from .serializers import *
from main.models import *

from django.contrib.auth import get_user_model
UserModel = get_user_model()

from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins

from django.http import Http404


@api_view(['GET'])
def getRoutes(request):
	routes = [
		'GET /api/',
		'[GET | POST] /api/users',
		'[GET | PUT | DELETE] /api/users/<int:pk>/'
		'[GET | POST] /api/subjects/',
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
class SubjectDetailsV2(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, partial=True, **kwargs)

