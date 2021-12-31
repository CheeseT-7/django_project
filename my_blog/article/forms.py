#!/user/bin/env python
# coding=utf-8
"""
@project : django_project
@author  : CheeseT
#@file   : forms.py
#@ide    : PyCharm
#@time   : 2021-12-29 16:48:13
"""
# 引入表单类
from django import forms
# 引入文章模型
from .models import ArticlePost


# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型的来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
