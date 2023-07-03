from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("forum/", Forum.as_view(), name="forum"),
    path("forum/add_comment/", add_comment, name="add_comment"),
    path("forum/del_comment/<int:pk>", del_comment, name="del_comment"),
    path("contact/", contact, name="contact"),
    path("get-ip/", get_client_ip),
]
