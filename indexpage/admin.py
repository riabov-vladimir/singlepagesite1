from django.contrib import admin
from .models import CvText


@admin.register(CvText)
class CvTextAdmin(admin.ModelAdmin):
    pass
