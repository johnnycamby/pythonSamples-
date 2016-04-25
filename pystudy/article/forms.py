from django.forms import ModelForm
from article.models import Article, Comment

__author__ = 'johnny'



class ArticleForm(ModelForm):

    class Meta:
        model = Article
        exclude = ['likes']
        #fields = ('title', 'body', 'pub_date')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')



