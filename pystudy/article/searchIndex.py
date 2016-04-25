__author__ = 'johnny'

from haystack.constants import Indexable
from haystack.indexes import SearchIndex
import datetime
from haystack import indexes
from article.models import Article

class ArticleIndex(SearchIndex, Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(auto_now_add=True, blank=True)

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()