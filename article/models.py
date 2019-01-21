# from django.db import models
#
# # Create your models here.
#
# class Article(models.Model):
#     title = models.CharField(max_length=30,null=False) #文章标题
#     # types = models.ForeignKey(Atype,null=False,on_delete=models.CASCADE)
#     content = models.CharField(max_length=100,null=True) #内容描述
#     content = models.TextField() #文章内容
#     create_time = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'article'

from django.db import models

# 栏目
class Column(models.Model):
    # c = models.ForeignKey('self',max_length=100,verbose_name='栏目',on_delete=models.CASCADE)
    nums = models.CharField(max_length=20,unique=True,verbose_name='栏目编码')
    sort = models.CharField(max_length=20,null=False,unique=True,verbose_name='栏目分类名称')

# 文章
class Article(models.Model):
    # a = models.ForeignKey(Column,max_length=200, verbose_name='文章',on_delete=models.CASCADE)
    title = models.CharField(max_length=20,unique=True,verbose_name="标题")
    content =models.CharField(max_length=10000,null=False,verbose_name="内容")
    describe = models.CharField(max_length=200,null=False,verbose_name="描述")
    keyword = models.CharField(max_length=100,null=False,verbose_name='关键字')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')



