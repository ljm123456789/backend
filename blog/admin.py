from django.contrib import admin
from .models import Article
from .models import Users

admin.site.register(Article)
admin.site.register(Users)