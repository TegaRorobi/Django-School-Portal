from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import *
from rest_framework import permissions 
from .permissions import *

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	sent_messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	received_messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = UserModel
		fields = [field.name for field in model._meta.fields] + ['sent_messages', 'received_messages']


class SubjectSerializer(serializers.ModelSerializer):
	grades_taught_in = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Subject 
		fields = ['label', 'grades_taught_in']


class GradeSerializer(serializers.ModelSerializer):
	students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta: 
		model = Grade 
		fields = ['id', 'label', 'subjects', 'students', 'teachers']

class AllMessagesSerializer(serializers.ModelSerializer):
	sender = serializers.ReadOnlyField(source='sender.__str__')
	receiver = serializers.ReadOnlyField(source='receiver.__str__')
	class Meta:
		model = Message 
		fields = ['id', 'content', 'sender', 'receiver', 'timestamp']

class SentMessageSerializer(serializers.ModelSerializer):
	receiver_display = serializers.CharField(source='receiver.__str__', read_only=True)
	class Meta:
		model = Message 
		fields = ['id', 'content', 'receiver', 'receiver_display', 'timestamp']


class ReceivedMessageSerializer(serializers.ModelSerializer):
	sender_display = serializers.CharField(source='sender.__str__', read_only=True)
	class Meta:
		model = Message 
		fields = ['id', 'content', 'sender', 'sender_display', 'timestamp']
