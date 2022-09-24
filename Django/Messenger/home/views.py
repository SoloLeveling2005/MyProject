from django.shortcuts import render



def home(request):
    login = request.POST["login"]
    password = request.POST["password"]

    return render(request, "home/home.html", {"login": login, "password": password})
