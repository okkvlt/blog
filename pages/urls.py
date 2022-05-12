from django.urls import path

from .views import (author, category, day, index, month, pid, posts, sobre,
                    traducoes, year)

urlpatterns = [
    path("", index),
    path("posts", posts),
    path("traducoes", traducoes),
    path("sobre", sobre),

    path("posts/id/<int:pid>", pid),

    path("posts/<int:year>", year),  # year
    path("posts/<int:year>/<int:month>", month),  # month
    path("posts/<int:year>/<int:month>/<int:day>", day),  # day

    path("posts/author/<slug:author>", author),

    path("posts/categoria/<slug:category>", category),
]
