from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Admin, Register,Packages


def TravelManagementhome(request):
    return render(request, "TravelManagementhome.html")


def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]  # gets user name
        pwdd = request.POST["pwd"]
        flag = Register.objects.filter(name=name, password=pwdd).values()
        if flag:
            if name == "k":
                messages.info(request,"this is admin ttm page")
                return render(request, "adminhome.html")


        if flag:

            return render(request, "TravelManagementhome.html")
        else:
            messages.info(request, "your crendentials are not correct ")
            return render(request, "loginfail.html")


def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]

    if pwd == cpwd:
        if Register.objects.filter(username=uname).exists():
            messages.info(request, "username existing...")
            return render(request, "register.html")
        elif Register.objects.filter(email=email).exists():
            messages.info(request, "email existing...")
            return render(request, "registar.html")
        else:
            user = Register.objects.create(name=name, address=addr, email=email, phnumber=phno, username=uname,
                                           password=pwd)
            user.save()
            messages.info(request, "user created...")
            return render(request, "login.html")
def checkpackages(request):
    if request.method == "POST":
         tcode = request.POST["tourcode"]
         tname= request.POST["tourname"]
         tpack = request.POST["tourpackage"]
         tdesc = request.POST["desc"]
         pack = Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
         pack.save()
         messages.info(request,"Data inserted  sucessfully ")
         return render(request , "package.html")
    else:
        messages.info(request,"data is not inserted")
        return render(request, "package.html")






