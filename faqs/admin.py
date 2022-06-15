from django.contrib import admin
from .models import Question


@admin.register(Question)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("title",)
