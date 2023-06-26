from django.contrib import admin

from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'pin_top', 'created_at', 'published_date')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)