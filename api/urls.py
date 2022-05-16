from django.urls import path

from .views import *

urlpatterns = [
    path("posts", posts),
    path("search", search),
    path("books", books)
]
