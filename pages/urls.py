from django.urls import path

from .views import index, pid, posts, sobre, traducoes

urlpatterns = [
    path("", index),
    path("posts", posts),
    path("traducoes", traducoes),
    path("sobre", sobre),
    path("posts/<int:pid>", pid),
]
