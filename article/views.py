# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def detail(request,id):

    try:
        article = Article.objects.get(id=str(id))

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article.html', {'article': article})


def about_me(request):
    return render(request, 'aboutme.html')


def search_tag(request, tag):
    try:
        article_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'article_list': article_list})



class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/articles/"
    description = "RSS feed - blog"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
