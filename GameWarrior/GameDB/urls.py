from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("home/", Home.as_view(), name="home"),
    path("game/<str:slug>/", GetGame.as_view(), name="single"),
    path("games/", AllGames.as_view(), name="allgames"),
    path("search/", Search.as_view(), name="Search")
]
