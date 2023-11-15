from django.contrib import admin
from .models import *

admin.site.register(Subject)
admin.site.register(Grade)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
	model = TeacherProfile
	list_display = 'user', 'qualifications', 'subject_specializations_', 'grades_'
	
	@admin.display()
	def subject_specializations_(self, obj):
		return str([subject.label for subject in obj.subject_specializations.all()]).replace('\'', '')
	@admin.display()
	def grades_(self, obj):
		return str([grade.label for grade in obj.grades.all()]).replace('\'', '')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
	model = StudentProfile
	list_display = 'user', 'image', 'grade'

	@admin.display()
	def subjects_(self, obj):
		return str([subject.label for subject in obj.subjects.all()]).replace('\'', '')

@admin.register(AdminProfile)
class AdminprofileAdmin(admin.ModelAdmin):
	model = AdminProfile 
	list_display = 'user', 'image', 'position'

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
	model = Term 
	list_display = 'label', 'start_date', 'end_date'

@admin.register(StudentTermReport)
class StudentTermReportAdmin(admin.ModelAdmin):
	model = StudentTermReport
	list_display = 'student', 'grade', 'term', 'average', 'remark'


@admin.register(SubjectResult)
class SubjectResultAdmin(admin.ModelAdmin):
	model = SubjectResult
	list_display = 'student_', 'subject', 'term_report', 'first_test', 'second_test', 'exam', 'percentage'

	@admin.display()
	def student_(self, obj):
		return str(obj.term_report.student)