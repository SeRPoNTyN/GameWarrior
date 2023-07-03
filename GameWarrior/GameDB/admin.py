from django.utils.safestring import mark_safe
from .models import *
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GameAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = GameAdminForm
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug", "category", "get_image", "created_at", "views"]
    list_display_links = ["id", "title"]
    list_filter = ["category", "tag"]
    search_fields = ["title", "description", "tag", "category"]
    readonly_fields = ["views", "rating", "get_image"]
    fields = ["title", "slug", "description", "developer", "category", "tag", "image", "get_image", "rating", "views", "created_at"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width ='50'>")
        return "-"

    get_image.short_description = "Image"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tags, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)

