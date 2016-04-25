__author__ = 'johnny'

from django.conf.urls import patterns, include, url

urlpatterns = patterns ('',
    url(r'^$', 'appMain.views.home', name='main_home'),)
