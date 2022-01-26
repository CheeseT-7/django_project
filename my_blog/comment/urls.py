#!/user/bin/env python
# coding=utf-8
"""
@project : django_project
@author  : CheeseT
#@file   : urls.py
#@ide    : PyCharm
#@time   : 2022-01-24 11:39:42
"""
from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]
