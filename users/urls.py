from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
    path('',views.userlogin,name="userlogin"),
    path('register/',views.user_register,name="register"),
    path('sign-up/',views.user_sign_up_post,name="usersign"),
]