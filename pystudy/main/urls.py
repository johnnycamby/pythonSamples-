__author__ = 'johnny'

from django.conf.urls import patterns, include, url
from main.forms import ContactForm1, ContactForm2, ContactForm3
from main.views import ContactWizard


urlpatterns = patterns ('',
    url(r'^$', 'main.views.home', name='pystudy_home'),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3]),),
   #url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3]), name='main_contact'),

                        )


