# workflow_engine/admin.py

from django.contrib import admin
from .models import Workflow, Task, Link

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')  # Fields to display in the admin list view
    search_fields = ('name',)  # Search functionality

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'workflow', 'state')  # Fields to display in the admin list view
    list_filter = ('workflow', 'state')  # Filter options
    search_fields = ('name',)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('source', 'target')  # Fields to display in the admin list view
    search_fields = ('source__name', 'target__name')  # Search by task names

# Register models with the admin site
admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Link, LinkAdmin)
