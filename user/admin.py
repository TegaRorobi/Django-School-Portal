from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import ngettext
from django.contrib import messages

UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
	model = UserModel
	list_display = ('name', 'gender', 'username', 'account_type', 'is_superuser', 'passkey')

	@admin.action(description="Change selected users' account type to 'Admin'")
	def update_account_admin(self, request, queryset):
		updated = queryset.update(account_type='admin')
		self.message_user(
			request, 
			ngettext(
				f"{updated} user's account successfully changed to 'admin'",
				f"{updated} users account successfully changed to 'admin'",
				updated
			),
			messages.SUCCESS
		)

	@admin.action(description="Change selected users' account type to 'Student'")
	def update_account_student(self, request, queryset):
		updated = queryset.update(account_type='student')
		self.message_user(
			request, 
			ngettext(
				f"{updated} user's account type successfully changed to 'student'",
				f"{updated} users account type successfully changed to 'student'",
				updated
			),
			messages.SUCCESS
		)

	@admin.action(description="Change selected users' account type to 'Educator'")
	def update_account_educator(self, request, queryset):
		updated = queryset.update(account_type='educator')
		self.message_user(
			request, 
			ngettext(
				f"{updated} user's account successfully changed to educator",
				f"{updated} users account successfully changed to educator",
				updated
			),
			messages.SUCCESS
		)

	actions=['update_account_admin', 'update_account_student', 'update_account_educator']

