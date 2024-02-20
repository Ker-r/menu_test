from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu


@admin.register(Menu)
class MenuMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
