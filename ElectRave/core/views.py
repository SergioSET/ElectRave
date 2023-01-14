from django.shortcuts import render

def home(request):
    return render(
        request,
        "home.html",
        {
            "title": "ElectRave page",
        },
    )

def login(request):
    return render(
        request,
        "login.html",
        {
            "title": "ElectRave login page",
        },
    )

def register(request):
    return render(
        request,
        "register.html",
        {
            "title": "ElectRave register page",
        },
    )