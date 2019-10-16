from django.contrib import admin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'content',)


# admin.site.regiester(Article, ArticleAdmin)