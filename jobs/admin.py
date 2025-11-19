from django.contrib import admin
from .models import UserProfile, Job

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'company', 'phone']
    list_filter = ['user_type']
    search_fields = ['user__username', 'company']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'job_type', 'posted_date', 'is_active']
    list_filter = ['job_type', 'is_active', 'posted_date']
    search_fields = ['title', 'company', 'location', 'description']
    date_hierarchy = 'posted_date'
