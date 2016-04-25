from django.db import models
from datetime import datetime

# Create your models here.
from django.db.models import Model
from time import time

def get_upload_file_name(instance, filename):
    return 'uploads/%s_%s' % (str(time()).replace('.','_'), filename)

'''
def get_upload_file_name(instance , filename):
    with open('uploads/', 'wb+')as destination:
        for chunk in filename.chunks():
            destination.write(chunk)
'''

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'articles/get/%i/' % self.id
        #return 'get_article/%i' % self.id


class Comment(Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)
    article = models.ForeignKey(Article)
