
from django.urls import path, include
from .views import *


urlpatterns = [
    path("reviews/", GetRevs.as_view(), name="reviews"),
    path("create-review/", create_review, name="create-review"),
    path("review/<str:game_slug>/<str:slug>", GetReview.as_view(), name="review"),
]
