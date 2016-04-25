__author__ = 'johnny'

# ===========  pip install django-tastypie =============================
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from article.models import Article


class ArticleResource(ModelResource):

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = {'title': ALL}
        #filtering = {'title': 'contains'}






