from django.utils.safestring import mark_safe
from .models import *
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = NewsAdminForm
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug", "category", "get_image", "created_at", "views"]
    list_display_links = ["id", "title"]
    list_filter = ["category", "tag"]
    search_fields = ["title", "content", "tag", "author"]
    readonly_fields = ["views", "created_at", "get_image", "likes"]
    fields = ["title", "slug", "content", "author", "category", "tag", "image", "get_image", "views", "created_at", "likes"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width ='50'>")
        return "-"

    get_image.short_description = "Image"


class ReviewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Review
        fields = '__all__'


class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = NewsAdminForm
    save_as = True
    save_on_top = True
    list_display = ["id", "title", "slug", "author", "game", "created_at", "views", "score"]
    list_display_links = ["id", "title"]
    list_filter = ["tag", "game"]
    search_fields = ["title", "content", "tag", "author"]
    readonly_fields = ["views", "created_at", "likes", "score"]
    fields = ["title", "slug", "content", "author", "game", "tag", "views", "created_at", "likes", "score"]


admin.site.register(News, NewsAdmin)
admin.site.register(Review, ReviewAdmin)
