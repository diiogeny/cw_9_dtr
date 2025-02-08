from django.contrib import admin
from .models import Ad, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "status", "author", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)

