from django.contrib import admin
from .models import Lesson
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    summernote_fields = "body"
    prepopulated_fields = {"slug": ("title",)}
