#!/user/bin/env python
# coding=utf-8
"""
@project : django_project
@author  : CheeseT
#@file   : urls.py
#@ide    : PyCharm
#@time   : 2021-12-19 12:36:36
"""

# 引入path
from django.urls import path
# 引入views.py
from . import views

# 正在部署的应用app的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
]
