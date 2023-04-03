from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    summernote_fields = ('body',)
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        CommentInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
 