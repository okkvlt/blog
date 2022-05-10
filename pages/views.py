
from django.shortcuts import render

from pages.models import *
from pages.utils.utils import Utils

# Create your views here.


Utils = Utils()

config = Utils.get_config()
archive = Utils.get_archives()
colors = Utils.get_colors()
categorias = Utils.get_categorys()


def index(request):
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
    }

    return render(request, "index.html", index)


def posts(request):
    posts = Utils.get_posts()

    posts = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "posts": posts,
    }

    return render(request, "posts.html", posts)


def traducoes(request):
    livros = Utils.get_books()
    
    traducoes = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
    }

    return render(request, "traducoes.html", traducoes)


def sobre(request):
    about = Utils.get_about()
    
    sobre = {
        "config": config,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "about": about,
    }

    return render(request, "sobre.html", sobre)
    