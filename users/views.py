from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Profile, State, Order
from products.models import Product, Wishlist, AddToCart
from django.db.models import Count
import stripe
from django.contrib import messages
from django.conf import settings

title = {}
stripe.api_key = settings.SECRET_KEY # key for stripe

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
            if username == "" and userpass == "":
                dect['message'] = "Invalid"
                return render(req, "userlogin.html", dect)
            user = authenticate(username=username,password=userpass)

            if user is not None:
                login(req, user)
                req.session['uid'] = user.id
                return redirect("home")
            else:
                dect['message'] = "Invalid"
                return render(req, "userlogin.html", dect)
        return render(req, '404.html', status=404)


def log_out(req):
    logout(req)
    return redirect("userlogin")


@login_required(login_url='/')
def home_index(req):
    id = req.session['uid']
    try:
        wishes = Wishlist.objects.filter(user_id_id=id).count()
        cart = AddToCart.objects.filter(user_id_id=id).count()
        pros = Product.objects.all()
        product = {'products': pros, 'wish': wishes, 'cart': cart}
        product['header'] = "OnShop"
        return render(req, "home.html", product)
    except:
        return render(req, '404.html', status=404)


data = {}
# User Profile functions..................................
@login_required(login_url='/')
def user_profile(req):
    user_id = req.session['uid']
    try:
        try:
            user_profile = Profile.objects.get(user_id=user_id)
        except Profile.DoesNotExist:
            user_profile = None
        user = User.objects.get(id = user_id)
        state = State.objects.all()
        wishes_count = Wishlist.objects.filter(user_id_id=user_id).count()
        cart_count = AddToCart.objects.filter(user_id_id=user_id).count()
        context = {
            'userprofile': user_profile,
            'state': state,
            'wish': wishes_count,
            'cart': cart_count,
            'header': "Profile",
            "user": user
        }
        return render(req, "user_profile.html", context)
    
    except User.DoesNotExist:
        return render(req, '404.html', status=404)


@login_required(login_url='/')
def useraddrss(req,id):
    id = req.session['uid']
    if req.method == "POST":
        useraddrss = req.POST['useraddrss']
        userpin = req.POST['userpin']
        userdist = req.POST['userdist']
        userstate = req.POST['userstate']
        prof = Profile(user_id=id, address=useraddrss,
                       user_pin=userpin, user_dist=userdist, user_state=userstate)
        prof.save()
        return redirect("profile")


@login_required(login_url='/')
def edituseraddrss(req,id):
    id = req.session['uid']
    p = Profile.objects.get(user_id=id)
    if req.method == "POST":
        useraddrss = req.POST['useraddrss']
        userpin = req.POST['userpin']
        userdist = req.POST['userdist']
        userstate = req.POST['userstate']
        try:
            prof = Profile(id=p.id, user_id=id, address=useraddrss,
                       user_pin=userpin, user_dist=userdist, user_state=userstate)
            prof.save()
            return redirect("profile")
        except:
            return redirect("profile")


# edit profile.............................................
@login_required(login_url='/')
def editUserProfile(req):
    uid = req.session['uid']
    if req.method == "POST":
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['uemail']
        username = req.POST['username']
        User.objects.filter(id=uid).update(
            first_name=fname, last_name=lname, email=email, username=username)
        return redirect("profile")


# products...............................................

@login_required(login_url='/')
def product_details(req, id):
    data = req.session['uid']
    wishes = Wishlist.objects.filter(user_id_id=data).count()
    cart = AddToCart.objects.filter(user_id_id=data).count()
    prod = Product.objects.get(id=id)
    details = {'product': prod, 'wish': wishes, 'cart': cart}
    return render(req, "product_details.html", details)

#wishlist.....................................................
@login_required(login_url='/')
def wishlist(req, id):
    allpro = {}
    if req.method == "POST":
        wishlist_val = req.POST['wishlist_val']
        if wishlist_val == '0':
            return redirect('home')
        else:
            wishes = Wishlist.objects.filter(user_id_id=id).count()
            cart = AddToCart.objects.filter(user_id_id=id).count()
            wish = Wishlist.objects.filter(user_id_id=id)
            allpro['data'] = wish
            allpro['wish'] = wishes
            allpro['cart'] = cart
            return render(req, "wishlist.html", allpro)


@login_required(login_url='/')
def add_wishlist(req, pid):
    k = req.session['uid']
    getpro = Product.objects.get(id=pid)
    count = 1
    try:
        Wishlist.objects.filter(product_id_id=pid).get(user_id_id=k)
    except:
        count = 0
    if req.method == "POST":
        if count == 1:
            return redirect('home')
        else:
            wish = Wishlist(user_id_id=k, product_id_id=pid, p_img=getpro.p_img,
                            product_category=getpro.p_category, product_name=getpro.p_name, product_price=getpro.p_price)
            wish.save()
            return redirect('home')


@login_required(login_url='/')
def delete_wish(req, wid):
    allpro = {}
    k = req.session['uid']
    if req.method == "POST":
        Wishlist.objects.filter(id=wid).delete()
    wishes = Wishlist.objects.filter(user_id_id=k).count()
    cart = AddToCart.objects.filter(user_id_id=k).count()
    wish = Wishlist.objects.filter(user_id_id=k)
    allpro['data'] = wish
    allpro['wish'] = wishes
    allpro['cart'] = cart
    return render(req, "wishlist.html", allpro)


#cart functions......................................................................
@login_required(login_url='/')
def add_to_cart(req, uid):
    alldata = {}
    getcart = AddToCart.objects.filter(user_id_id=uid)
    wishes = Wishlist.objects.filter(user_id_id=uid).count()
    cart = AddToCart.objects.filter(user_id_id=uid).count()
    alldata['data'] = getcart
    alldata['wish'] = wishes
    alldata['cart'] = cart
    return render(req, "add_to_cart.html", alldata)
    


@login_required(login_url='/')
def add_cart_data(req, pid):
    k = req.session['uid']
    getpro = Product.objects.get(id=pid)
    if req.method == "POST":
        cart = AddToCart(user_id_id=k, product_id_id=pid, p_img=getpro.p_img,
                             product_category=getpro.p_category, product_name=getpro.p_name, product_price=getpro.p_price)
        cart.save()
        return redirect('home')


@login_required(login_url='/')
def delete_cart(req, cid):
    alldata = {}
    k = req.session['uid']
    if req.method == "POST":
        AddToCart.objects.filter(id=cid).delete()
    wishes = Wishlist.objects.filter(user_id_id=k).count()
    cart = AddToCart.objects.filter(user_id_id=k).count()
    cart2 = AddToCart.objects.filter(user_id_id=k)
    alldata['wish'] = wishes
    alldata['data'] = cart2
    alldata['cart'] = cart
    return render(req, "add_to_cart.html", alldata)


# Product Order....................................................................
@login_required(login_url='/')
def order_product(req,pid):
    def get_data(self, **argu):
        context = get_data(**argu)
        context['key'] = settings.PUBLISHABLE_KEY
        return context
    userpro = {}
    k = req.session['uid']
    try:
        user_profile = Profile.objects.get(user_id=k)
        order_product = Product.objects.filter(id = pid)
        wishes = Wishlist.objects.filter(user_id_id=k).count()
        cart = AddToCart.objects.filter(user_id_id=k).count()
        userpro['users'] = user_profile
        userpro['pro'] = order_product
        userpro['cart'] = cart
        userpro['wish'] = wishes
        return render(req,"order_product.html",userpro)
    except:
        return redirect('product',pid)


#payment gateway implimentation..........................................
@login_required(login_url='/')
def payment(req,pid):
    if req.method == "POST":
        k = req.session['uid']
        f_name = req.POST['f_name']
        l_name = req.POST['l_name']
        email= req.POST['email']
        address = req.POST['address']
        pin = req.POST['pin']
        dist = req.POST['dist']
        state =req.POST['state']
        pro_name = req.POST['pro_name']
        price = req.POST['price']
        if address is not None:
            order = Order(user_address = address, user_pin = pin,user_state = state,user_dist = dist,pro_name = pro_name,pro_price = price, user_id_id = k, status = "pending",user_email = email,user_fisrt_name = f_name,user_last_name = l_name,pro_quantity = str(1))
            order.save()
            stripe.PaymentIntent.create(
                description="Shopping",
                shipping={
                    "name": "Biplab Ganguly",
                    "address": {
                        "line1": "510 Townsend St",
                        "postal_code": "723132",
                        "city": "Durgapur",
                        "state": "West Bengal",
                        "country": "INDIA",
                    },
                },
                amount=500,
                currency="usd",
                payment_method_types=["card"],
            )
            pro = Product.objects.get(id = pid)
            data = int(pro.p_quantity) -1
            check = Product(p_quantity = str(data),id= pid,p_name = pro.p_name,p_category = pro.p_category,p_img = pro.p_img,p_desc = pro.p_desc,p_price = pro.p_price)
            check.save()
            userpro ={}
            wishes = Wishlist.objects.filter(user_id_id=k).count()
            cart = AddToCart.objects.filter(user_id_id=k).count()
            userpro['cart'] = cart
            userpro['wish'] = wishes
            userpro['uid'] = k
            return render(req,"paymentsuccess.html",userpro)
        else:
            return redirect('product',pid)
    


@login_required(login_url='/')
def check_order_list(req,uid):
    alldata = {}
    order = Order.objects.filter(user_id_id = uid).filter(status = "pending")
    alldata["order_data"] = order
    wishes = Wishlist.objects.filter(user_id_id=uid).count()
    cart = AddToCart.objects.filter(user_id_id=uid).count()
    alldata['cart'] = cart
    alldata['wish'] = wishes
    return render(req,"order.html",alldata)


@login_required(login_url='/')
def order_receive(req,oid):
    k = req.session['uid']
    order_pro = Order.objects.get(id = oid)
    if req.method == "POST":
        check = Order(id = oid,user_address = order_pro.user_address, user_pin = order_pro.user_pin,user_state = order_pro.user_state,user_dist = order_pro.user_dist,pro_name = order_pro.pro_name,pro_price = order_pro.pro_price, user_id_id = k, status = "received",user_email = order_pro.user_email,user_fisrt_name = order_pro.user_fisrt_name,user_last_name = order_pro.user_last_name)
        check.save()  
        return redirect('order_list', k)


# order history..........................................................
@login_required(login_url='/')
def order_history(req):
    k = req.session['uid']
    hist = Order.objects.filter(user_id_id = k).filter(status = "received")
    alldata = {}
    alldata["order_data"] = hist
    wishes = Wishlist.objects.filter(user_id_id=k).count()
    cart = AddToCart.objects.filter(user_id_id=k).count()
    alldata['cart'] = cart
    alldata['wish'] = wishes
    return render(req,"order_history.html",alldata)


@login_required(login_url='/')
def delete_history(req):
    k = req.session['uid']
    if req.method == "POST":
        Order.objects.filter(user_id_id = k).filter(status = "received").delete()
        return redirect('order_hist')


# cart buy .....................................................
@login_required(login_url='/')
def cart_buy(req):
    k = req.session['uid']
    data = AddToCart.objects.all().filter(user_id_id = k).values('product_id_id','p_img','product_name','product_price','product_category').annotate(total=Count('id'))
    wishes = Wishlist.objects.filter(user_id_id=k).count()
    cart = AddToCart.objects.filter(user_id_id=k).count()
    alldata = {
        'data' : data
    }
    alldata['cart'] = cart
    alldata['wish'] = wishes
    return render(req,"cart_buy.html",alldata)



@login_required(login_url='/')
def cart_payment(req):
    k = req.session['uid']
    if req.method == "POST":
        for i in range(1, len(req.POST)):
            pid = req.POST.get(f'pid_{i}')
            tl = req.POST.get(f'total_{i}')
            print(pid, tl)
            if(pid is not None):
                checkdata = Product.objects.get(id = pid)
                user = User.objects.get(id= k)
                pro = Profile.objects.get(user_id = k)
                qunt = checkdata.p_quantity
                total_item = int(tl)
                data_item = int(qunt)
                if total_item <= data_item: 
                    stripe.PaymentIntent.create(
                    description="Shopping",
                    shipping={
                        "name": "Biplab Ganguly",
                        "address": {
                        "line1": "510 Townsend St",
                        "postal_code": "723132",
                        "city": "Durgapur",
                        "state": "West Bengal",
                        "country": "INDIA",
                        },
                    },
                        amount=500,
                        currency="usd",
                        payment_method_types=["card"],
                    )
                    data = int(qunt) - int(tl)
                    order = Order(user_address = pro.address, user_pin = pro.user_pin,user_state = pro.user_state,user_dist = pro.user_dist,pro_name = checkdata.p_name,pro_price = checkdata.p_price, user_id_id = k, status = "pending",user_email = user.email,user_fisrt_name = user.first_name,user_last_name = user.last_name,pro_quantity = tl )
                    order.save()
                    check = Product(p_quantity = str(data),id= pid,p_name = checkdata.p_name,p_category = checkdata.p_category,p_img = checkdata.p_img,p_desc = checkdata.p_desc,p_price = checkdata.p_price)
                    check.save()
                    AddToCart.objects.filter(user_id_id=k).delete()
                else:
                    messages.error(req, 'Items are Out of Stock')
                    return redirect('cart_buy')
            else:
                if i <= len(req.POST):
                    userpro ={}
                    wishes = Wishlist.objects.filter(user_id_id=k).count()
                    cart = AddToCart.objects.filter(user_id_id=k).count()
                    userpro['cart'] = cart
                    userpro['wish'] = wishes
                    userpro['uid'] = k
                    return render(req,"paymentsuccess.html",userpro)
                else:
                    messages.error(req, 'No items are found')
                    return redirect('cart_buy')     
    
            
