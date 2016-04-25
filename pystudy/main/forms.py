from django import forms
from django.forms import Form

__author__ = 'johnny'


class ContactForm2(Form):
    sender = forms.EmailField()

class ContactForm3(Form):
    message = forms.CharField(widget=forms.Textarea)

class ContactForm1(Form):
    subject = forms.CharField(max_length=100)