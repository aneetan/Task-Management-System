from rest_framework import serializers
from .models import Project, ProjectUserRole

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']

class ProjectUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUserRole
        fields = '__all__'

