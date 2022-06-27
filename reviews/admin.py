from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("created_on", "author", "approved")
    search_fields = ["title", "author"]
    actions = ["approve_review"]

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
