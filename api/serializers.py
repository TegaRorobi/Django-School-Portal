from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import *

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	# sent_messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# received_messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = UserModel
		fields = '__all__'

class UserSubSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = 'id', 'name', 'email'


class GradeSubSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Grade 
		fields = 'id', 'label'


class SubjectSubSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = 'id', 'label'


class StudentProfileSerializer(serializers.ModelSerializer):
	user_ = UserSubSerializer(source='user', required=False, read_only=True)
	grade_ = GradeSubSerializer(source='grade', required=False, read_only=True)
	subjects_ = SubjectSubSerializer(source='subjects', required=False, many=True, read_only=True)
	class Meta:
		model = StudentProfile 
		fields = '__all__'
		extra_kwargs = {
			'user': {'write_only':True, 'required':True},
			'grade': {'write_only':True, 'required':True},
			'subjects': {'write_only':True, 'required':True},
		}


class TeacherProfileSerializer(serializers.ModelSerializer):
	user_ = UserSubSerializer(source='user', read_only=True)
	grades_ = GradeSubSerializer(source='grades', many=True, read_only=True)
	subject_specializations_ = SubjectSubSerializer(source='subject_specializations', many=True, read_only=True)
	class Meta:
		model = TeacherProfile
		fields = '__all__'
		extra_kwargs = {
			'user': {'write_only':True},
			'grades': {'write_only':True},
			'subject_specializations': {'write_only':True},
		}


class AdminProfileSerializer(serializers.ModelSerializer):
	user_ = UserSubSerializer(source='user', many=False, read_only=True)
	class Meta:
		model = AdminProfile 
		fields = '__all__'
		extra_kwargs = {
			'user': {'write_only':True},
		}


class GradeSerializer(serializers.ModelSerializer):
	students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta: 
		model = Grade 
		fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
	grades_taught_in = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Subject 
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