from rest_framework.permissions import BasePermission
from .models import ProjectUserRole

class IsProjectAdmin(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_id')
        if not project_id:
            return False
        return ProjectUserRole.objects.filter(
            project_id = project_id, user =request.user, role='admin'
        ).exists()