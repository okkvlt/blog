from django.urls import path

from .views import index, posts, traducoes

urlpatterns = [
    path("", index),
    path("posts", posts),
    path("traducoes", traducoes),
]
