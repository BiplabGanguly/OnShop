from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
#   if req.method == "POST":
#         fname = req.POST['fname']
#         lname = req.POST['lname']
#         email = req.POST['email']
#         username = req.POST['username']
#         pass1 = req.POST['pass1'] 
#         pass2 = req.POST['pass2'] 

#         if pass1 == pass2:
#             newUser = User.objects.create_user(username = username,email = email,password = pass1)
#             newUser.first_name = fname
#             newUser.last_name = lname
#             newUser.save()
#             mess['mess'] = "user created"
#             return render(req,"index.html",mess)
#         else:
#             mess['mess'] = "something went wrong"
#             return render(req,"signin.html",mess)

def userlogin(req):
    return render(req,"userlogin.html")

def user_register(req):
    return render(req,"user_register.html")

def user_sign_up_post(req):
    if req.method == "POST":
        ufirstname = req.POST['ufirstname']
        ulastname = req.POST['ulastname']
        useremail = req.POST['useremail']
        username = req.POST['username']
        userpass1 = req.POST['userpass1']
        userpass2 = req.POST['userpass2']

        print(ufirstname,ulastname,useremail,username,userpass1,userpass2)
        return redirect('userlogin')