from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_pinned',
        'created_at'
    )

    search_fields = (
        'title',
        'content'
    )

    list_filter = (
        'is_pinned',
    )

    ordering = (
        'is_pinned',
        'created_at',
    )
