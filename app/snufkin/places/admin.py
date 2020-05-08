from django.contrib import admin
from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "user",)
    search_fields = ("name",)
    list_filter = ("user",)
