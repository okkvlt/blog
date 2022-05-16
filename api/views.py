from urllib import response

from django.http import HttpResponse, JsonResponse
from pages.models import *

from .utils.utils import Utils

# Create your views here.

Utils = Utils()


def posts(request):
    methods = {
        "all": [],
        "id": ["id"],
        "category": ["category"],
        "author": ["author"],
        "year": ["year"],
        "month": [
            "year",
            "month",
        ],
        "day": [
            "year",
            "month",
            "day"
        ],
    }

    if Utils.check(request=request, methods_params=methods):
        return JsonResponse(Utils.check(request=request, methods_params=methods))

    modes = {
        "all": Posts.objects.order_by("-date"),
        "id": Posts.objects.filter(id=request.GET.get("id")),
        "author": Posts.objects.filter(author__username=request.GET.get("author")).order_by("-date"),
        "category": Posts.objects.filter(categoria__nome__iexact=request.GET.get("category")).order_by("-date"),

        "year": Posts.objects.filter(date__year=request.GET.get("year")).order_by("-date"),

        "month": Posts.objects.filter(date__year=request.GET.get("year"),
                                      date__month=request.GET.get("month")).order_by("-date"),

        "day": Posts.objects.filter(date__year=request.GET.get("year"),
                                    date__month=request.GET.get("month"),
                                    date__day=request.GET.get("day")).order_by("-date"),
    }

    response = {}

    if request.GET.get("page") == None:
        posts = modes[request.GET["method"]]
    else:
        start = (int(request.GET.get("page")) - 1) * 5
        end = start + 5

        posts = modes[request.GET["method"]][start:end]

        if len(modes[request.GET["method"]][end:end+5]) > 0:
            response["more"] = True
        else:
            response["more"] = False

    posts_list = []

    for post in posts:
        posts_list.append(post.as_dict())

    if not posts_list:
        response["status"] = "error"
        response["info"] = "nothing found!"
    else:
        response["status"] = "ok"
        response["posts"] = posts_list

    return JsonResponse(response)


def books(request):
    methods = {
        "all": [],
        "id": ["id"],
        "author": ["author"],
        "category": ["category"],
    }

    if Utils.check(request=request, methods_params=methods):
        return JsonResponse(Utils.check(request=request, methods_params=methods))

    modes = {
        "all": Livros.objects.order_by("-id"),
        "id": Livros.objects.filter(id=request.GET.get("id")),
        "author": Livros.objects.filter(author__iexact=request.GET.get("author")).order_by("-id"),
        "category": Livros.objects.filter(category__nome__iexact=request.GET.get("category")).order_by("-id"),
    }

    response = {}

    if request.GET.get("page") == None:
        books = modes[request.GET["method"]]
    else:
        start = (int(request.GET.get("page")) - 1) * 15
        end = start + 15

        books = modes[request.GET["method"]][start:end]

        if len(modes[request.GET["method"]][end:end+5]) > 0:
            response["more"] = True
        else:
            response["more"] = False

    books_list = []

    for book in books:
        books_list.append(book.as_dict())

    if not books_list:
        response["status"] = "error"
        response["info"] = "nothing found!"
    else:
        response["status"] = "ok"
        response["books"] = books_list

    return JsonResponse(response)


def search(request):
    methods = {
        "books": ["key"],
        "posts": ["key"],
        "users": ["key"],
    }

    if Utils.check(request=request, methods_params=methods):
        return JsonResponse(Utils.check(request=request, methods_params=methods))

    if request.GET.get("page"):
        page = int(request.GET.get("page"))
    else:
        page = None

    modes = {
        "books": Utils.search(method="books",
                              key=request.GET.get("key"),
                              page=page),

        "posts": Utils.search(method="posts",
                              key=request.GET.get("key"),
                              page=page),
    }

    response = modes[request.GET["method"]]

    if not response:
        return JsonResponse({
            "status": "error",
            "info": "nothing found!"
        })

    return JsonResponse(response)
