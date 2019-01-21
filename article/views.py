from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# 文章
from django.urls import reverse

from article.forms import AddArticleForm
from article.models import Article
from user.models import User


def article(request):
    if request.method == 'GET':
        a =  Article.objects.all()
        return render(request,'back/article.html',{'a':a})

#添加文章
def add_article(request):
    if request.method == 'GET':
        return render(request,'back/add-article.html')

    if request.method == 'POST':
        # 标题表单校验
        form = AddArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Article.objects.create(
                title = title,
                content = content,
            )
            return HttpResponseRedirect(reverse('article:article'))
        # article_content = request.POST.get('article-content')



# 文章栏目
def category(request):
    if request.method == 'GET':
        return render(request,'back/category.html')

        # return render(request,'front/index.html')


def delete_a(request,id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('article:article'))

def index(request):
    if request.method == 'GET':
        a = Article.objects.all()
        return render(request,'front/index.html',{'a':a})
