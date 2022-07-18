from django.contrib import admin
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'mail', 'password', 'time_create')
    list_display_links = ('id', 'nickname')
    search_fields = ('nickname', 'mail')
    list_filter = ('time_create',)
admin.site.register(Women, WomenAdmin)

