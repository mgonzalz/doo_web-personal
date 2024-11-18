from django.contrib import admin
from .models import Experience

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Experience, ExperienceAdmin)
