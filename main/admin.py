from django.contrib import admin
from .models import Subject, Grade, TeacherProfile, StudentProfile

admin.site.register(Subject)
admin.site.register(Grade)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
	model = TeacherProfile
	list_display = ['user', 'image', 'grades_']

	@admin.display()
	def grades_(self, obj):
		return str([grade.label for grade in obj.grades.all()]).replace('\'', '')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
	model = StudentProfile
	list_display = ['user', 'image', 'grade', 'subjects_']

	@admin.display()
	def subjects_(self, obj):
		return str([subject.label for subject in obj.subjects.all()]).replace('\'', '')