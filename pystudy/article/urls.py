
__author__ = 'johnny'

from django.conf.urls import patterns , include, url
from article.api import ArticleResource

article_resource = ArticleResource()
# http://127.0.0.1:8000/articles/api/article/?format=json
# http://127.0.0.1:8000/articles/api/article/1/?format=json
# http://127.0.0.1:8000/articles/api/article/?format=json&title__contains=3


urlpatterns = patterns('article.views',
                       url(r'^all/$', 'articles', name='all_articles' ),
                       url(r'^search/$', 'search', name='search_article' ),
                       url(r'^api/', include(article_resource.urls) ),
                       url(r'^get/(?P<article_id>\d+)/$', 'article', name= 'get_article'),
                       #url(r'^edit/(?P<article_id>\d+)/$', 'edit', name= 'edit_article'),
                       url(r'^create/$', 'create', name='create_article'),
                       url(r'^comment/(?P<article_id>\d+)$', 'comment', name='create_comment'),
                       url(r'^delete/(?P<comment_id>\d+)$', 'delete', name='delete_comment')
                       )
