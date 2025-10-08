from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'created_at', 'review_text')
    search_fields = ('movie__title',)
    list_filter = ('stars', 'created_at')
