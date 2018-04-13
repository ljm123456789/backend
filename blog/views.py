from django.shortcuts import render
from django.http import HttpResponse
from . import models
#import models
#from .models import Article

def index(request):
    articles = models.Article.objects.all()
    name = request.session.get('name', default='default')
    password = request.session.get('passwd', default='default')
    #name = request.POST.get('username', 'haha')
    #password = request.POST.get('password', 'haha')
    return render(request, 'index.html', {'articles': articles, 'username':name, 'password':password})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})


def article_edit_page(request, article_id):
    #str方法将参数转化为字符串，避免因传递类型差异引起的错误
    # -1代表是新增博客，否则是编辑博客，编辑博客时需要传递博客对象到页面并显示
    if str(article_id) == '0':
        return render(request, 'article_edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_edit_page.html', {'article': article})



def article_edit_page_action(request):
    title = request.POST.get('title', '默认标题')     ##get是根据参数名称从form表单页获取内容
    content = request.POST.get('content', '默认内容')
    article_id = request.POST.get('article_id_hidden', 'ar')
    ##保存数据
    ##如果是0，标记新增，使用create方法，否则使用save方法
    ##新增是返回首页，编辑是返回详情页
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        ##数据保存完成，返回首页
        articles = models.Article.objects.all()
        return render(request, 'index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'article_page.html', {'article': article}) 

def login(request):
    return render(request, 'login.html')

def handlinglogin(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'article_page.html', {'article': article})
    #return HttpResponse('hello')
    #name = request.POST.get('username', 'haha')
    #passwd = request.POST.get('password', '123')
    #models.Users.objects.create(name=name, passwd=passwd)
    #return HttpResponse('hello')

    #articles = models.Article.objects.all()
    #return render(request, 'index.html', {'articles': articles})

def another(request):
    #article = models.Article.objects.get(pk=1)
    #return render(request, 'article_page.html', {'article': article})
    name = request.POST.get('username', 'haha')
    passwd = request.POST.get('password', '123')

    request.session['name'] = name
    request.session['passwd'] = passwd

    models.Users.objects.create(name=name, passwd=passwd)

    article= models.Article.objects.all()
    return render(request, 'index.html', {'articles': article, 'username':name, 'password':passwd})
