from django import forms

from article.models import Article


class AddArticleForm(forms.Form):

    title = forms.CharField(max_length=20,
                              min_length=1,
                              required=True,
                              error_messages={
                                  'required': '文章标题必须填写',
                                  'max_length': '文章标题不能超过20字符',
                                  'min_length': '文章标题不能短于5字符'
                              })

    content = forms.CharField(max_length=10000,
                                  min_length=1,
                                  required=True,
                                  error_messages={
                                      'required': '文章内容必须填写',
                                      'max_length': '文章内容不能超过10000字符',
                                      'min_length': '文章内容不能短于1字符'
                              })

    # def clean_a_title(self):
    #     title = self.cleaned_data('a_title')
    #     article = Article.ojects.filter(title=title).first()
    #     if article:
    #         raise forms.ValidationError({'title':'给文章标题已经存在，请重新给标题取名'})
    #     return self.cleaned_data