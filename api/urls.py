
from django.urls import re_path

from .views import *
from .aliases import *

from rest_framework_simplejwt.views import (
    token_obtain_pair,
    token_refresh,
    token_blacklist)


auth_paths = (
    re_path('^auth/login/?$', token_obtain_pair, name='api-login'),
    re_path('^auth/login/refresh/?$', token_refresh, name='api-login-refresh'),
    re_path('^auth/logout/?$', token_blacklist, name='api-logout'),)

user_paths = (
    re_path('^users/?$', UsersViewSet.as_view(LIST_CREATE), name='users-list'),
    re_path('^users/(?P<pk>\d+)/?$', UsersViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='user-detail'),)

student_profile_paths = (
    re_path('^student-profiles/?$', StudentProfilesViewSet.as_view(LIST_CREATE), name='student-profiles-list'),
    re_path('^student-profiles/(?P<pk>\d+)/?$', StudentProfilesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='student-profile-detail'),)

teacher_profile_paths = (
    re_path('^teacher-profiles/?$', TeacherProfilesViewSet.as_view(LIST_CREATE), name='teacher-profiles-list'),
    re_path('^teacher-profiles/(?P<pk>\d+)/?$', TeacherProfilesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='teacher-profile-detail'),)

admin_profile_paths = (
    re_path('^admin-profiles/?$', AdminProfilesViewSet.as_view(LIST_CREATE), name='admin-profiles-list'),
    re_path('^admin-profiles/(?P<pk>\d+)/?$', AdminProfilesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='admin-profile-detail'),)

subject_paths = (
    re_path('^subjects/?$', SubjectsViewSet.as_view(LIST_CREATE), name='subjects-list'),
    re_path('^subjects/(?P<pk>\d+)/?$', SubjectsViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='subject-detail'),)

grade_paths = (
    re_path('^grades/?$', GradesViewSet.as_view(LIST_CREATE), name='grades-list'),
    re_path('^grades/(?P<pk>\d+)/?$', GradesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='grade-detail'),)

message_paths = (
    re_path('^messages/?$', AllMessagesViewSet.as_view(LIST), name='messages-list'),
    re_path('^messages/(?P<pk>\d+)/?$', AllMessagesViewSet.as_view(RETRIEVE), name='message-detail'),

    re_path('^messages/sent/?$', SentMessagesViewSet.as_view(LIST_CREATE), name='sent-messages-list'),
    re_path('^messages/sent/(?P<pk>\d+)/?$', SentMessagesViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='sent-message-detail'),

    re_path('^messages/received/?$', ReceivedMessagesViewSet.as_view(LIST), name='received-messages-list'),
    re_path('^messages/received/(?P<pk>\d+)/?$', ReceivedMessagesViewSet.as_view(RETRIEVE), name='received-message-detail'),)

term_paths = (
    re_path('^terms/?$', TermsViewSet.as_view(LIST_CREATE), name='terms-list'),
    re_path('^terms/(?P<pk>\d+)/?$', TermsViewSet.as_view(RETRIEVE_UPDATE), name='term-detail'),)

student_term_report_paths = (
    re_path('^term-reports/?$', StudentTermReportViewSet.as_view(LIST_CREATE), name='term-reports-list'),
    re_path('^term-reports/(?P<pk>\d+)/?$', StudentTermReportViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='term-report-detail'),)

subject_result_paths = (
    re_path('^subject-results/?$', SubjectResultViewSet.as_view(LIST_CREATE), name='subject-results-list'),
    re_path('^subject-results/(?P<pk>\d+)/?$', SubjectResultViewSet.as_view(RETRIEVE_UPDATE_DESTROY), name='subject-result-detail'),)

urlpatterns = [
    *auth_paths,
    *user_paths,
    *student_profile_paths,
    *teacher_profile_paths,
    *admin_profile_paths,
    *subject_paths,
    *grade_paths,
    *message_paths,
    *term_paths,
    *student_term_report_paths,
    *subject_result_paths
]