from django.urls import path

from article import views

urlpatterns = [
    # 文章
    path('article/',views.article,name='article'),
    # 添加文章
    path('add_article/', views.add_article, name='add_article'),
    # 文章栏目
    path('category/', views.category, name='category'),
    #删除
    path('delete_a/<int:id>/',views.delete_a,name='delete_a'),
    # 渲染到前端
    path('index/',views.index,name='index'),

]