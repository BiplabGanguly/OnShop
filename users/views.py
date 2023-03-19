from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Profile, State
from products.models import Product

title = {}


def userlogin(req):
    title['header'] = "log-in"
    return render(req, "userlogin.html", title)


def user_register(req):
    title['header'] = "sign-up"
    return render(req, "user_register.html", title)


mess = {}


def user_sign_up_post(req):
    if req.method == "POST":
        ufirstname = req.POST['ufirstname']
        ulastname = req.POST['ulastname']
        useremail = req.POST['useremail']
        username = req.POST['username']
        userpass1 = req.POST['userpass1']
        userpass2 = req.POST['userpass2']

        if userpass1 == userpass2:
            newUser = User.objects.create_user(
                username=username, email=useremail, password=userpass1)
            newUser.first_name = ufirstname
            newUser.last_name = ulastname
            newUser.save()
            mess['mess'] = "user created"
            return render(req, "userlogin.html", mess)
        else:
            mess['mess'] = "something went wrong"
            return render(req, "user_register.html", mess)


dect = {}
def login_user_post(req):
    if req.method == "POST":
        username = req.POST['username']
        userpass = req.POST['userpass']
        useremail = req.POST['useremail']
        user = authenticate(username=username,
                            password=userpass, email=useremail)

        if user is not None:
            login(req, user)
            return redirect("home",user.id)
        else:
            dect['message'] = "Invalid"
            return render(req, "userlogin.html", dect)


def log_out(req):
    logout(req)
    return redirect("userlogin")



@login_required(login_url='')
def home_index(req,id):
    # wishes = Wishlist.objects.filter(user_id_id = id).count()
    pros = Product.objects.all()
    product={'products': pros}
    title['header'] = "OnShop"
    # req.session['wishdatas'] = wishes
    req.session['uid'] = id
    return render(req, "home.html",product)


data = {}
@login_required(login_url='')
def user_profile(req, id):
    user_profile = Profile.objects.filter(user_id=id)
    state = State.objects.all()
    # wishes = Wishlist.objects.filter(user_id_id = id).count()
    profile = {'userprofile': user_profile, 'state': state}
    title['header'] = "Profile"
    return render(req, "user_profile.html", profile)


@login_required(login_url='')
def useraddrss(req, id):
    if req.method == "POST":
            useraddrss = req.POST['useraddrss']
            userpin = req.POST['userpin']
            userdist = req.POST['userdist']
            userstate = req.POST['userstate']
            prof = Profile(user_id=id, address=useraddrss,
                       user_pin=userpin, user_dist=userdist, user_state=userstate)
            prof.save()
            return redirect("profile",id)



@login_required(login_url='')
def edituseraddrss(req, id):
    p = Profile.objects.get(user_id = id)
    if req.method == "POST":
            useraddrss = req.POST['useraddrss']
            userpin = req.POST['userpin']
            userdist = req.POST['userdist']
            userstate = req.POST['userstate']
            prof = Profile(id = p.id,user_id=id, address=useraddrss,
                       user_pin=userpin, user_dist=userdist, user_state=userstate)
            prof.save()
            return redirect("profile",id)
               

# edit profile
@login_required(login_url='')
def editUserProfile(req,uid):
    # p = User.objects.get(id = uid)
    if req.method == "POST":
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['uemail']
        username = req.POST['username']
        edituser = User.objects.filter(id = uid).update(first_name = fname,last_name = lname,email = email,username = username)
        # edituser.save()
        return redirect("profile",uid)


# products

@login_required(login_url='')
def product_details(req,id):
    # data = req.session['wishdatas']
    prod = Product.objects.get(id = id)
    details = {'product':prod}
    return render(req,"product_details.html",details)


@login_required(login_url='')
def wishlist(req,id):
    allpro = {}
    if req.method == "POST":
        wishlist_val = req.POST['wishlist_val']
        if wishlist_val == '0':
            return redirect('home',id)
        else:
            # wishes = Wishlist.objects.filter(user_id_id = id).count()
            # following = (u.following for u in Profile.objects.filter(user=request.user))
            # # posts = Post.objects.filter(user__in=following)
            # wish = Wishlist.objects.filter(user_id_id = id)
            prolist = Product.objects.select_related('wishlist')
            # allpro['uid'] = wish
            allpro['data'] = prolist
            # allpro['wish']= wishes
            return render(req,"wishlist.html",allpro)
    

@login_required(login_url='')
def add_wishlist(req,pid):
    if req.method == "POST":
        k = req.session['uid']
        # wish = Wishlist(user_id_id = k,product_id_id = pid)
        # wish.save()
        # return redirect('home',k)


