
from .serializers import *
from main.models import *
from .permissions import *

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response

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

	queryset = Message.objects.prefetch_related('sender', 'receiver').order_by('-date_created')
	serializer_class = AllMessagesSerializer
	permission_classes = [IsSuperUser]



class SentMessagesViewSet(viewsets.ModelViewSet):

	"API Viewset to get all sent messages of a particular user (the currently authenticated user), "\
	"retrieve specific messages, send new messages to other people, as well as update and delete them."

	serializer_class = SentMessageSerializer
	permission_classes = [permissions.IsAuthenticated]

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()

		if 'receiver_id' in request.query_params or 'to' in request.query_params:
			param = 'to' if 'to' in request.query_params else 'receiver_id'
			try:
				receiver_id = int(request.query_params.get(param))
				receiver = UserModel.objects.get(id=int(receiver_id))
			except ValueError:
				return Response({
					"error": f"Invalid '{param}' parameter. Expected an integer."
				}, status=status.HTTP_400_BAD_REQUEST)
			except UserModel.DoesNotExist:
				return Response({
					'error': f"Invalid '{param}' parameter. User with id '{receiver_id}' not found."
				}, status=status.HTTP_404_NOT_FOUND)
			
			queryset = queryset.filter(receiver=receiver)

		queryset = self.filter_queryset(queryset)

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
	
	def perform_create(self, serializer):
		return serializer.save(sender=self.request.user)
	
	def get_queryset(self):
		return Message.objects.prefetch_related('receiver').filter(sender=self.request.user).order_by('-date_created')



class ReceivedMessagesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

	"API Vievset to perform read operations on received messages, i.e getting all received messages, "\
	"retrieving the detail of a specific received message."

	serializer_class = ReceivedMessageSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		return Message.objects.prefetch_related('sender').filter(receiver=self.request.user).order_by('-date_created')


class TermsViewSet(
	mixins.ListModelMixin, mixins.CreateModelMixin, 
	mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
	viewsets.GenericViewSet):

	"API Viewset to list out all terms, create new terms, retrieve and update the details of a term."

	queryset = Term.objects.all().order_by('-start_date')
	serializer_class = TermSerializer
	permission_classes = [IsSuperUserOrReadOnly]


class StudentTermReportViewSet(viewsets.ModelViewSet):
	
	"API Viewset to list out, create, retrieve, update and delete student term reports."

	queryset = StudentTermReport.objects.prefetch_related('results', 'student', 'grade', 'term').order_by('student__user__name', 'student__user__email')
	serializer_class = StudentTermReportSerializer
	permission_classes = [IsAdminOrTeacherOrSuperUser]