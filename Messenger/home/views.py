from django.shortcuts import render
from .models import BD


def home(request):
    login = request.POST["login"]
    password = request.POST["password"]
    element = BD(login=login, password=password)
    element.save()
    return render(request, "home/home.html", {"login": login, "password": password})
