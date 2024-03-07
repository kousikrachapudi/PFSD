from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")

def loginpage(request):
    return render(request, "login.html")


def registrationpage(request):
    return render(request, "register.html")

def viewpackages(request):
    return render(request,"viewpackages.html")

def  insertpackages(request):
    return render(request,"insertpackages.html")