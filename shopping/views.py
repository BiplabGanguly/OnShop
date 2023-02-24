from django.shortcuts import render

def userlogin(req):
    return render(req,"userlogin.html")

def user_register(req):
    return render(req,"user_register.html")