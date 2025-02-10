from django.contrib import admin
from .models import WasteDetails, FrequencyType, DisposalMethod

@admin.register(WasteDetails)
class WasteDetailsAdmin(admin.ModelAdmin):
    list_display = ['producer', 'image','types_of_waste', 'quantity', 'frequency', 'disposal_method']
    search_fields = ['producer__username', 'types_of_waste', 'quantity']
    list_filter = ['types_of_waste', 'frequency', 'disposal_method', 'producer']

@admin.register(FrequencyType)
class FrequencyTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_custom']
    search_fields = ['name']
    list_filter = ['is_custom']

@admin.register(DisposalMethod)
class DisposalMethodAdmin(admin.ModelAdmin):
    list_display = ['method_name', 'is_custom']
    search_fields = ['method_name']
    list_filter = ['is_custom']