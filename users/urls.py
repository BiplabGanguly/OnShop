from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('',views.userlogin,name="userlogin"),
    path('register/',views.user_register,name="register"),
    path('sign-up/',views.user_sign_up_post,name="usersign"),
    path('login/',views.login_user_post,name="login"),
    path('onshop/',views.home_index,name="home"),
    path('logout/',views.log_out,name="logout"),
    path('profile/<id>',views.user_profile,name="profile"),
    path('address/<id>',views.useraddrss,name="useraddress"),
    path('editaddress/<id>',views.edituseraddrss,name="edituseraddress"),
]