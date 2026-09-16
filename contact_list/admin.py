from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactsAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_display_links =('first_name', 'last_name')