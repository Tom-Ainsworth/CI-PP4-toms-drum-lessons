from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ("author", "created_on", "approved")
    search_fields = ["title", "author"]
    summernote_fields = "body"
    actions = ["approve_review"]

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
