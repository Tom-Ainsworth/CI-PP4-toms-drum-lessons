from django.contrib import admin
from .models import Lesson
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ("title", "format", "author", "created_on")
    search_fields = ["title", "format", "author"]
    list_filter = ("format", "author", "status")
    summernote_fields = "body"
    prepopulated_fields = {"slug": ("title",)}
