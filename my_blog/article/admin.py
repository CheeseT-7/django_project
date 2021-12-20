from django.contrib import admin
# 导入ArticlePost
from .models import ArticlePost

# Register your models here.

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
