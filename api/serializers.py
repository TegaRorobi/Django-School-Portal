from rest_framework import serializers
from main.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject 
		fields = '__all__'