
from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
	"Custom permission that checks if a user is a SuperUser"

	def has_permission(self, request, view):
		return bool(request.user and request.user.is_authenticated and request.user.is_superuser)



class IsAdminOrSuperUser(permissions.BasePermission):
	"Custom permission that checks if a user is an AdminUser (is_staff=True) or SuperUser (is_superuser=True)"

	def has_permission(self, request, view):
		return bool(request.user and request.user.is_authenticated and 
			(request.user.is_staff or request.user.is_superuser))



class IsAdminOrSuperUserOrReadOnly(permissions.BasePermission):
	"Custom permission to grant edit access to only site admins or superusers otherwise read access."

	def has_permission(self, request, view):
		return bool(request.method in permissions.SAFE_METHODS or 
			(request.user and request.user.is_authenticated and 
				(request.user.is_staff or request.user.is_superuser)))



class IsAdminOrSuperUserOrOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return bool(request.method in permissions.SAFE_METHODS or (
			request.user==obj.user or (
				request.user.is_authenticated and ((
					request.user.is_staff or request.user.is_superuser)))))



class IsSuperUserOrOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return bool(request.method in permissions.SAFE_METHODS or (
			request.user==obj.user or (
				request.user.is_authenticated and request.user.is_superuser)))