from django.urls import path

from .views import index, posts, sobre, traducoes

urlpatterns = [
    path("", index),
    path("posts", posts),
    path("traducoes", traducoes),
    path("sobre", sobre),
]
