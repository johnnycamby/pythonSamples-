__author__ = 'johnny'

from django.conf.urls import patterns, include, url
from .views import SignUpView


urlpatterns = patterns('appUser.views',
                       url(r'^home$', 'home',name='user_home'),
                       url(r'^signup$', SignUpView.as_view(), name='user_signup'),
                       )
