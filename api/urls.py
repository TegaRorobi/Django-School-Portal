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