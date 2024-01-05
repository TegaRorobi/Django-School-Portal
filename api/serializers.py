from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import *

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	sent_messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	received_messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = UserModel
		fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):
	user_display = serializers.ReadOnlyField(source='user.__str__')
	grade_display = serializers.ReadOnlyField(source='grade.__str__')
	class Meta:
		model = StudentProfile 
		fields = '__all__'


class TeacherProfileSerializer(serializers.ModelSerializer):
	user_display = serializers.ReadOnlyField(source='user.__str__')
	class Meta:
		model = TeacherProfile 
		fields = '__all__'


class AdminProfileSerializer(serializers.ModelSerializer):
	user_display = serializers.ReadOnlyField(source='user.__str__')
	class Meta:
		model = AdminProfile 
		fields = '__all__'


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
		fields = '__all__'


class AllMessagesSerializer(serializers.ModelSerializer):
	sender = serializers.ReadOnlyField(source='sender.__str__')
	receiver = serializers.ReadOnlyField(source='receiver.__str__')
	class Meta:
		model = Message 
		fields = '__all__'


class SentMessageSerializer(serializers.ModelSerializer):
	receiver_display = serializers.ReadOnlyField(source='receiver.__str__')
	class Meta:
		model = Message 
		fields = '__all__'


class ReceivedMessageSerializer(serializers.ModelSerializer):
	sender_display = serializers.ReadOnlyField(source='sender.__str__')
	class Meta:
		model = Message 
		fields = '__all__'


class TermSerializer(serializers.ModelSerializer):
	class Meta:
		model = Term 
		fields = '__all__'


class StudentTermReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentTermReport
		fields = '__all__'


class SubjectResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubjectResult
		fields = '__all__'


class StudentTermReportSerializer(serializers.ModelSerializer):
	results = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = StudentTermReport 
		fields = '__all__'


class SubjectResultSerializer(serializers.ModelSerializer):
	student = serializers.ReadOnlyField(source='term_report.student.__str__')
	grade = serializers.ReadOnlyField(source='term_report.grade.__str__')

	class Meta:
		model = SubjectResult
		fields = '__all__'