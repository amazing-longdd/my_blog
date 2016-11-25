# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add = True)  # 博客日期
    content = models.TextField(blank = True, null = True)  # 博客文章正文

    def __unicode__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-date_time']