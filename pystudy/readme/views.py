__author__ = 'johnny'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('account/loggedin')
    else:
        return HttpResponseRedirect('accounts/invalid_login')

def loggedin(request):
    return render(request, 'loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
