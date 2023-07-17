from django.contrib import admin
from django.contrib.auth import get_user_model


UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
	model = UserModel
	list_display = ('username', 'is_staff', 'is_student', 'is_educator')