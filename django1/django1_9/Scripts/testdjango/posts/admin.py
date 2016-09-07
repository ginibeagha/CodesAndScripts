from django.contrib import admin

# Register your models here.
from .models import Post

def make_published(self, request, queryset):
    queryset.update(title='testing')
make_published.short_description = "Mark selected stories as published"

class PostModelAdmin(admin.ModelAdmin):
    list_display= ["title", "timestamp","updated"]
    list_filter=["title", "updated"]
    actions=[make_published]
    class Meta:
        model=Post

    

admin.site.register(Post, PostModelAdmin)