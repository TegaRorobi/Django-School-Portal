from django.urls import path, include
from .views import *

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'users', UsersViewSet)
# router.register(r'subjects', SubjectsViewSet)

app_name = 'api'
urlpatterns = [
	path('', getRoutes),

	# users
	path('v1/users/', UsersListV1.as_view(), name='users-list-v1'),
	path('v1/users/<int:pk>/', UserDetailsV1.as_view(), name='user-detail-v1'),
	path('v2/users/', UsersListV2.as_view(), name='users-list-v2'),
	path('v2/users/<int:pk>/', UserDetailsV2.as_view(), name='user-detail-v2'),
	path('v3/users/', UsersListV3.as_view(), name='users-list-v3'),
	path('v3/users/<int:pk>/', UserDetailsV3.as_view(), name='user-detail-v3'),

	# subjects
	path('v1/subjects/', SubjectsListV1.as_view(), name='subjects-list-v1'),
	path('v1/subjects/<int:pk>/', SubjectDetailsV1.as_view(), name='subject-detail-v1'),
	path('v2/subjects/', SubjectsListV2.as_view(), name='subjects-list-v2'),
	path('v2/subjects/<int:pk>/', SubjectDetailsV2.as_view(), name='subject-detail-v2'),

	# grades
	path('grades/', GradesList.as_view(), name='grades-list'),
	path('grades/<int:pk>/', GradeDetails.as_view(), name='grade-detail'),

	# messages
	path('messages/sent/', MessagesSent.as_view(), name='messages-sent'),
	path('messages/sent/<int:pk>/', SentMessageDetails.as_view(), name='sent-message-detail'),
	path('messages/received/', MessagesReceived.as_view(), name='messages-received'),
	path('messages/received/<int:pk>/', ReceivedMessageDetails.as_view(), name='received-message-detail'),

]

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)








LIST = {'get':'list'}
RETRIEVE = {'get':'retrieve'}
LIST_CREATE = {'get':'list', 'post':'create'}
RETRIEVE_UPDATE_DESTROY = {'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}
RETRIEVE_DESTROY = {'get':'retrieve', 'delete':'destroy'}


urlpatterns = format_suffix_patterns([
	path('', getRoutes, name='index'),

	#users
	path('users/', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
	path('users/<int:pk>/', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),

	#studentprofiles
	path('student-profiles/', StudentProfilesViewSet.as_view(LIST_CREATE), name='student-profiles-list'),
	path('student-profiles/<int:pk>/', StudentProfilesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='student-profile-detail'),

	#subjects
	path('subjects/', SubjectsViewSet.as_view(LIST_CREATE), name='subjects-list'),
	path('subjects/<int:pk>/', SubjectsViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='subject-detail'),

	#grades
	path('grades/', GradesViewSet.as_view(LIST_CREATE), name='grades-list'),
	path('grades/<int:pk>/', GradesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='grade-detail'),

	#messages
	path('messages/', AllMessagesViewSet.as_view(LIST), name='messages-list'),
	path('messages/sent/', SentMessagesViewSet.as_view(LIST_CREATE), name='sent-messages-list'),
	path('messages/sent/<int:pk>/', SentMessagesViewSet.as_view(RETRIEVE_DESTROY), name='sent-message-detail'),
	path('messages/received/', ReceivedMessagesViewSet.as_view(LIST), name='received-messages-list'),
	path('messages/received/<int:pk>/', ReceivedMessagesViewSet.as_view(RETRIEVE), name='received-message-detail'),

])