from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "start_date", "end_date")
    search_fields = ("name",)
    list_filter = ("user",)
