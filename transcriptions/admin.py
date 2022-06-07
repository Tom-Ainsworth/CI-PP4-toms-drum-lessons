from django.contrib import admin
from .models import Transcription


@admin.register(Transcription)
class TranscriptionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("song_name", "artist_name")}
    list_display = ("song_name", "artist_name", "author")
    search_fields = ["song_name", "artist_name", "author"]
