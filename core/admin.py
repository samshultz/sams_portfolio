from django.contrib import admin

from .models import Skills, TechStack, WorkExperience


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'company',
        'start_date',
        'end_date',
        'description',
    )
    list_filter = ('start_date', 'end_date')
