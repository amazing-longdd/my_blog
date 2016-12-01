# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#首页
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

#文章详情
def detail(request,id):

    try:
        article = Article.objects.get(id=str(id))

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article.html', {'article': article})



def about_me(request):
    return render(request, 'aboutme.html')


#按照tag分类显示
def search_tag(request, tag):
    try:
        article_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'article_list': article_list})


#所有的tag分类
def showAllTags(request):

    article_list = Article.objects.all();
    tags_list = []

    try:
        for article in article_list:

            if article.category not in tags_list:

                tags_list.append(article.category)

    except tags_list.DoesNotExist:
        raise Http404

    return render(request,'category_list.html',{'tags_list' : tags_list})


#RSS
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
