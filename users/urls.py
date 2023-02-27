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
    path('onshop/admin/',views.admin_panel,name="admin"),
    path('product/<id>',views.product_details,name="product"),
    path('wishlist/<id>',views.wishlist,name="wishlist"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)