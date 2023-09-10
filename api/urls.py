
from django.urls import path
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register('users', UsersViewSet, 'users')
router.register('student-profiles', StudentProfilesViewSet, 'student-profiles')
router.register('teacher-profiles', TeacherProfilesViewSet, 'teacher-profiles')
router.register('admin-profiles', AdminProfilesViewSet, 'admin-profiles')
router.register('subjects', SubjectsViewSet, 'subjects')
router.register('grades', GradesViewSet, 'grades')
router.register('messages', AllMessagesViewSet, 'messages')
router.register('messages/sent', SentMessagesViewSet, 'sent-messages')
router.register('messages/received', ReceivedMessagesViewSet, 'received-messages')


urlpatterns = router.urls