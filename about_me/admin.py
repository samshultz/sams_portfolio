from django.contrib import admin

from .models import AboutMe


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'phone')
