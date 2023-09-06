from django.urls import path
from .views import getRoutes, getSubjects

app_name = 'api'

urlpatterns = [
	path('', getRoutes),
	path('subjects/', getSubjects),
]