from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import Subject

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject 
		fields = '__all__'

