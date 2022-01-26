#!/user/bin/env python
# coding=utf-8
"""
@project : django_project
@author  : CheeseT
#@file   : forms.py
#@ide    : PyCharm
#@time   : 2022-01-24 11:33:18
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
