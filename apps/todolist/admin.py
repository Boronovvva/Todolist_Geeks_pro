from django.contrib import admin

from apps.todolist.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'completed', 'created_at')
    list_filter = ('title','description', 'completed', 'created_at')
