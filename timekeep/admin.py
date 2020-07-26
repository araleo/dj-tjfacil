from django.contrib import admin
from .models import Task

class TimekeepAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Task, TimekeepAdmin)
