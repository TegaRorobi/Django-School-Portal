from django.db import models, IntegrityError
from django.utils.translation import gettext as _

from django.contrib.auth import get_user_model
UserModel = get_user_model()

from base.models import BaseModel


class Subject(BaseModel):

	label = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.label



class Grade(BaseModel):

	GRADE_LABEL_CHOICES = [
		('Kindergarten 1', 'Kindergarten 1'),
		('Kindergarten 2', 'Kindergarten 2'),
		('Nursery 1', 'Nursery 1'),
		('Nursery 2', 'Nursery 2'),
		('Primary 1', 'Primary 1'),
		('Primary 2', 'Primary 2'),
		('Primary 3', 'Primary 3'),
		('Primary 4', 'Primary 4'),
		('Primary 5', 'Primary 5'),
	]
	label = models.CharField(max_length=15,choices=GRADE_LABEL_CHOICES)
	subjects = models.ManyToManyField(Subject, related_name='grades_taught_in')

	def __str__(self):
		return self.label



class TeacherProfile(BaseModel):

	user = models.OneToOneField(UserModel, related_name='teacher_profile', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/teacher_profiles', null=True, blank=True)
	grades = models.ManyToManyField(Grade, related_name='teachers')
	bio = models.TextField(_('Biography'), default='Teacher @ the school portal.', null=True)

	qualifications = models.CharField(max_length=500, null=True)
	subject_specializations = models.ManyToManyField(Subject, related_name='specialized_teachers')

	def save(self, *args, **kwargs):
		if self.user.is_student:
			raise IntegrityError("It is illegal to attach a teacher profile to a user object already attached to a student profile")
		self.user.is_teacher = True
		self.user.save()
		super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)



class StudentProfile(BaseModel):

	user = models.OneToOneField(UserModel, related_name='student_profile', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/student_profiles', null=True, blank=True)
	grade = models.ForeignKey(Grade, related_name='students', on_delete=models.PROTECT)
	subjects = models.ManyToManyField(Subject, related_name='offering_students')
	bio = models.TextField(_('Biography'), default='Student @ the school portal.')\

	def save(self, *args, **kwargs):
		try:
			if self.user.teacher_profile:
				raise IntegrityError("Illegal Operation: The selected user object is already attached to a teacher profile")
		except:
			self.user.is_student = True
			# making sure all selected subjects are offered by the selected grade.
			# O(n) time complexity and O(n) space complexity, where n is the number of
			# subjects offered by the grade which is fairly constant
			hashset = set(subject.label for subject in self.grade.subjects.all())
			for subject in self.subjects.all():
				if subject.label not in hashset:
					raise IntegrityError(f"Subject {subject.label} is not offered by the selected grade: {self.grade}")
			super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)



class AdminProfile(BaseModel):

	user = models.OneToOneField(UserModel, related_name='admin_profile', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/admin_profiles', null=True, blank=True)
	bio = models.TextField(_('Biography'), default="Site admin @ the school portal.")

	position = models.CharField(max_length=300, null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.user.is_student:
			# log an error message
			raise IntegrityError("It is illegal to attach an admin profile to a user object already attached to a student profile")
		self.user.is_admin = True
		self.user.save()
		super().save(*args, **kwargs)

	def __str__(self):
		return str(self.user)



class Message(BaseModel):

	sender = models.ForeignKey(UserModel, related_name='sent_messages', on_delete=models.CASCADE)
	receiver = models.ForeignKey(UserModel, related_name='received_messages', on_delete=models.CASCADE)
	content = models.TextField()

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return f"{self.sender} -> {self.receiver}"



class Term(BaseModel):

	LABEL_CHOICES = [
		('first', 'First'), 
		('second', 'Second'), 
		('third', 'Third')
	]

	label = models.CharField(max_length=6, choices=LABEL_CHOICES)
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self) -> str:
		return (
			f"{self.label.title()} term, "
			f"{self.start_date.strftime('%a, %d %b %Y')} -> "
			f"{self.end_date.strftime('%a, %d %b %Y')}")



class StudentTermReport(BaseModel):

	student = models.ForeignKey(StudentProfile, related_name='term_reports', on_delete=models.CASCADE)
	grade = models.ForeignKey(Grade, related_name='term_reports', on_delete=models.CASCADE)
	term = models.ForeignKey(Term, related_name='student_reports', on_delete=models.CASCADE)
	remark = models.CharField(max_length=200, default="Awaiting remark...")

	def average(self):
		# O(n) time, O(1) space
		total = num_results = 0
		for result in self.results.all():
			total += result.percentage()
			num_results += 1
		try:
			return total/num_results
		except ZeroDivisionError:
			return 0
	
	def __str__(self):
		return f"{self.term.label.title()} term report for {self.student.__str__()}. {self.term.start_date} -> {self.term.end_date}"



class SubjectResult(BaseModel):

	term_report = models.ForeignKey(StudentTermReport, related_name='results', on_delete=models.CASCADE, null=True, blank=True)
	subject = models.ForeignKey(Subject, related_name='student_results', on_delete=models.CASCADE)

	first_test = models.IntegerField(default=0)
	second_test = models.IntegerField(default=0)
	exam = models.IntegerField(default=0)

	def percentage(self):
		return (self.first_test + self.second_test + self.exam) / 100
