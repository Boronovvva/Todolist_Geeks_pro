from rest_framework import serializers

from apps.todolist.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description','completed', 'created_at')