from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'contact_info', 'address', 'organization_name']
    search_fields = ['user__username', 'user_type', 'contact_info', 'address', 'organization_name']
    list_filter = ['user_type']
    raw_id_fields = ['user']  # Added for better user selection in admin