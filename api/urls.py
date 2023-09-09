
from django.urls import path
from .views import *

from rest_framework import routers

# LIST = {'get':'list'}
# RETRIEVE = {'get':'retrieve'}
# LIST_CREATE = {'get':'list', 'post':'create'}
# RETRIEVE_UPDATE_DESTROY = {'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}
# RETRIEVE_DESTROY = {'get':'retrieve', 'delete':'destroy'}


# urlpatterns = [
# 	path('', getRoutes, name='index'),

# 	#users
# 	path('users/', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
# 	path('users/<int:pk>/', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),

# 	#studentprofiles
# 	path('student-profiles/', StudentProfilesViewSet.as_view(LIST_CREATE), name='student-profiles-list'),
# 	path('student-profiles/<int:pk>/', StudentProfilesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='student-profile-detail'),

# 	#subjects
# 	path('subjects/', SubjectsViewSet.as_view(LIST_CREATE), name='subjects-list'),
# 	path('subjects/<int:pk>/', SubjectsViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='subject-detail'),

# 	#grades
# 	path('grades/', GradesViewSet.as_view(LIST_CREATE), name='grades-list'),
# 	path('grades/<int:pk>/', GradesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='grade-detail'),

# 	#messages
# 	path('messages/', AllMessagesViewSet.as_view(LIST), name='messages-list'),
# 	path('messages/sent/', SentMessagesViewSet.as_view(LIST_CREATE), name='sent-messages-list'),
# 	path('messages/sent/<int:pk>/', SentMessagesViewSet.as_view(RETRIEVE_DESTROY), name='sent-message-detail'),
# 	path('messages/received/', ReceivedMessagesViewSet.as_view(LIST), name='received-messages-list'),
# 	path('messages/received/<int:pk>/', ReceivedMessagesViewSet.as_view(RETRIEVE), name='received-message-detail'),

# ]

router = routers.DefaultRouter()

router.register('users', UsersViewSet, 'users')
router.register('student-profiles', StudentProfilesViewSet, 'student-profiles')
router.register('subjects', SubjectsViewSet, 'subjects')
router.register('grades', GradesViewSet, 'grades')
router.register('messages', AllMessagesViewSet, 'messages')
router.register('messages/sent', SentMessagesViewSet, 'sent-messages')
router.register('messages/received', ReceivedMessagesViewSet, 'received-messages')



# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(router.urls)
urlpatterns = router.urls