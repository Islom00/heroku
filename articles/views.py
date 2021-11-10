from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "article_list.html"
    model = Article
    context_object_name = "articles"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "article_detail.html"
    model = Article
    context_object_name = "article"


