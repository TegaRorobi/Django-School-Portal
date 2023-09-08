
from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
	"Custom permission to grant edit access to only site admins otherwise read access."

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True 
		return bool(request.user and request.user.is_staff)

