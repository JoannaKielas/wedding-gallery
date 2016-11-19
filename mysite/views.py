from django.contrib.auth import authenticate
from django.contrib.auth.views import login, logout
from django.shortcuts import HttpResponseRedirect, HttpResponse


def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')

    else:
        return HttpResponse('Logowanie niepoprawne')


def my_logout(request):
   logout(request)
   return HttpResponseRedirect('/')
