from django.contrib import admin

from .models import Character, Favorite


class FavoriteInline(admin.TabularInline):
    model = Favorite


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    inlines = [FavoriteInline]
    list_filter = ["name"]
    list_display = ["name", "id"]
