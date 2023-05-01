from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.userlogin,name="userlogin"),
    path('register/',views.user_register,name="register"),
    path('sign-up/',views.user_sign_up_post,name="usersign"),
    path('login/',views.login_user_post,name="login"),
    path('onshop/<id>',views.home_index,name="home"),
    path('logout/',views.log_out,name="logout"),
    path('profile/<id>',views.user_profile,name="profile"),
    path('address/<id>',views.useraddrss,name="useraddress"),
    path('editaddress/<id>',views.edituseraddrss,name="edituseraddress"),
    path('product/<id>',views.product_details,name="product"),
    path('wishlist/<id>',views.wishlist,name="wishlist"),
    path('addwish/<pid>',views.add_wishlist,name="addwish"),
    path('editprofile/<uid>',views.editUserProfile,name="edituser"),
    path('deletewish/<wid>',views.delete_wish,name="deletewish"),
    path('cart/<uid>',views.add_to_cart,name="cart"),
    path('addcart/<pid>',views.add_cart_data,name="cartdata"),
    path('deletecart/<cid>',views.delete_cart,name="deletecart"),
    path('order_product/<pid>',views.order_product,name="orderpro"),
    path('order_process/<pid>',views.payment,name="payment"),
    path('order_list/<uid>',views.check_order_list,name="order_list"),
    path('order_receive/<oid>',views.order_receive,name="receive"),
    path('order_history',views.order_history,name="order_hist"),
    path('delete/history',views.delete_history,name="delete_history"),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)