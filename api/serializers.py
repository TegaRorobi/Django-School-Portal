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


class StudentProfileSerializer(serializers.ModelSerializer):
	user_display = serializers.ReadOnlyField(source='user.__str__')
	class Meta:
		model = StudentProfile 
		fields = [field.name for field in model._meta.fields] + ['subjects', 'user_display']


class TeacherProfileSerializer(serializers.ModelSerializer):
	user_display = serializers.ReadOnlyField(source='user.__str__')
	class Meta:
		model = TeacherProfile 
		fields = [field.name for field in model._meta.fields] + ['grades', 'subject_specializations', 'user_display']


class AdminProfileSerializer(serializers.ModelSerializer):
	user_display = serializers.ReadOnlyField(source='user.__str__')
	class Meta:
		model = AdminProfile 
		fields = [field.name for field in model._meta.fields] + ['user_display']


class SubjectSerializer(serializers.ModelSerializer):
	grades_taught_in = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Subject 
		fields = '__all__'


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
	receiver_display = serializers.ReadOnlyField(source='receiver.__str__')
	class Meta:
		model = Message 
		fields = ['id', 'content', 'receiver', 'receiver_display', 'timestamp']


class ReceivedMessageSerializer(serializers.ModelSerializer):
	sender_display = serializers.ReadOnlyField(source='sender.__str__')
	class Meta:
		model = Message 
		fields = ['id', 'content', 'sender', 'sender_display', 'timestamp']


class TermReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = TermReport
		fields = '__all__'


class SubjectResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubjectResult
		fields = '__all__'
