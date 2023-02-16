from django.shortcuts import render

def userinterface(req):
    return render(req,"userindex.html")