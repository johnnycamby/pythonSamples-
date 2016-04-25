"""pystudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
import main

admin.autodiscover()

urlpatterns = patterns ('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'main.views.home', name='pystudy_home'),
    url(r'^$', include('main.urls')),
    url(r'^search/$', include('haystack.urls')),
    #url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
    url(r'^articles/', include('article.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^user/', include('user.urls')),)

urlpatterns += patterns('django.contrib.auth.views',
                        url(r'^login/$', 'login',
                            {'template_name': 'login.html'},
                            name='pystudy_login'
                            ),
                        url(r'^logout/$', 'logout',
                            {'next_page': 'pystudy_home'},
                            name='pystudy_logout'
                            ),)