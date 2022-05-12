
from django.shortcuts import render
from django.http import HttpResponse

from pages.models import *
from pages.utils.utils import Utils

# Create your views here.


Utils = Utils()


def index(request):
    config = Utils.get_config()
    archive = Utils.get_archives()
    colors = Utils.get_colors()
    categorias = Utils.get_categorys()
    livros = Utils.get_books()

    posts = Utils.get_posts(3)
    apresentacao = Utils.get_apresentation()
    livros = Utils.get_books(3)

    index = {
        "config": config,
        "posts": posts,
        "apresentacao": apresentacao,
        "archive": archive,
        "livros": livros,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
    }

    return render(request, "index.html", index)


def posts(request):
    config = Utils.get_config()
    archive = Utils.get_archives()
    colors = Utils.get_colors()
    categorias = Utils.get_categorys()
    livros = Utils.get_books()

    response = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
    }

    if not "q" in request.GET:
        response["posts"] = Utils.get_posts()

        return render(request, "posts.html", response)

    response["posts"] = Utils.search_for_posts(request.GET["q"])
    response["query"] = request.GET["q"]

    return render(request, "posts.html", response)


def traducoes(request):
    config = Utils.get_config()
    archive = Utils.get_archives()
    colors = Utils.get_colors()
    categorias = Utils.get_categorys()
    livros = Utils.get_books()

    response = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
    }

    return render(request, "traducoes.html", response)


def sobre(request):
    config = Utils.get_config()
    archive = Utils.get_archives()
    colors = Utils.get_colors()
    categorias = Utils.get_categorys()
    livros = Utils.get_books()

    about = Utils.get_about()

    response = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
        "about": about,
    }

    return render(request, "sobre.html", response)


def pid(request, pid):
    config = Utils.get_config()
    archive = Utils.get_archives()
    colors = Utils.get_colors()
    categorias = Utils.get_categorys()
    livros = Utils.get_books()

    post = Utils.get_post_byid(pid)

    response = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
        "post": post,
    }

    return render(request, "sub/post.html", response)
