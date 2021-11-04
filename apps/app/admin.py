from django.contrib import admin
from .models import Memo

class MemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'created_datetime')
admin.site.register(Memo, MemoAdmin)
