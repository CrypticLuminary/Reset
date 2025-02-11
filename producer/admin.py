from django.contrib import admin
from .models import PostWasteDetails

@admin.register(PostWasteDetails)
class AdminPostWastedetails(admin.ModelAdmin):
    list_display = ['name','description','image','price']
    search_fields = ['name','description','price']
    list_filter = ['name','price']
    raw_id_fields = ['name']
    

