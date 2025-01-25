from django.contrib import admin
from .models import User, Category, Article, Comment, Like, Notification

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('date_joined',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    ordering = ('created_at',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')
    list_filter = ('category',)
    ordering = ('created_at',)
    autocomplete_fields = ('author', 'category')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'article', 'created_at', 'id')
    search_fields = ('content', 'author__username', 'article__title')
    ordering = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_at')
    search_fields = ('user__username', 'article__title')
    ordering = ('created_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'content', 'created_at', 'is_read')
    search_fields = ('recipient__username', 'content')
    list_filter = ('is_read',)
    ordering = ('created_at',)
