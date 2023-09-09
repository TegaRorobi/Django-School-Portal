from django.urls import path, include
from .views import *

LIST = {'get':'list'}
RETRIEVE = {'get':'retrieve'}
LIST_CREATE = {'get':'list', 'post':'create'}
RETRIEVE_UPDATE_DESTROY = {'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}
RETRIEVE_DESTROY = {'get':'retrieve', 'delete':'destroy'}


urlpatterns = [
	path('', getRoutes, name='index'),

	#users
	path('users/', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
	path('users/<int:pk>/', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),

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

]

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)