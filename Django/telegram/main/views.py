from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    content = {

    }
    return render(request, "main.html", content)

def hi(request):
    return HttpResponse("<a href='/main'>Перейти на страницу index</a>")

