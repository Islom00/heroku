from django.contrib import admin

from articles.models import Article


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["title", "summary", "created_at", "author"]
