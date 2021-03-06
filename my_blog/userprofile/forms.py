#!/user/bin/env python
# coding=utf-8
"""
@project : django_project
@author  : CheeseT
#@file   : forms.py
#@ide    : PyCharm
#@time   : 2022-01-05 20:16:28
"""
# 引入表单类
from django import forms
# 引入User模型
from django.contrib.auth.models import User
# 引入Profile模型
from .models import Profile


# 登录表单，继承了forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 注册表单
class UserRegisterForm(forms.ModelForm):
    # 复写User的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError('密码输入不一致，请重试。')


# Profile对应表单
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')
