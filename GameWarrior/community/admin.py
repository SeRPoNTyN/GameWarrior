from django.contrib import admin
from .models import Comments
# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "content", "created_at"]
    list_display_links = ["id", "content"]
    list_filter = ["user"]
    search_fields = ["user", "content"]
    readonly_fields = ["created_at"]
    fields = ["user", "content", "created_at"]
    save_as = True
    save_on_top = True


admin.site.register(Comments, CommentsAdmin)
