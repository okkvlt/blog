
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from pages.models import *
from pages.utils.utils import Utils

# Create your views here.


Utils = Utils()


def index(request):
    if request.method != "GET":
        return HttpResponse("Método não permitido nesta página!", status=405)

    config = Utils.get_config()
    archive = Utils.get_archives()
    colors = Utils.get_colors()
    categorias = Utils.get_categorys()
    livros = Utils.get_books() #widget

    apresentacao = Utils.get_apresentation()
    livros = Utils.get_books(3) #last books
    
    response = {
        "config": config,
        "apresentacao": apresentacao,
        "archive": archive,
        "colors": colors,
        "categorias": categorias,
        "livros": livros,
    }
    
    posts = requests.get("http://127.0.0.1:8000/api/posts?method=all&page=1").json()
    
    if not posts.get("status"):
        response["posts"] = posts

    return render(request, "index.html", response)


def posts(request):
    if request.method != "GET":
        return HttpResponse("Método não permitido nesta página!")

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

    key = request.GET.get("q")

    if not key:
        r = requests.get("http://127.0.0.1:8000/api/posts?method=all&page=1").json()

        if not r.get("status"):
            response["posts"] = r

        response["method"] = "all"

        return render(request, "posts.html", response)

    r = requests.get(f'http://127.0.0.1:8000/api/search?method=posts&key={key}&page=1').json()

    if not r.get("status"):
        response["posts"] = r

    response["query"] = request.GET["q"]
    response["method"] = "search"

    return render(request, "posts.html", response)


def traducoes(request):
    if request.method != "GET":
        return HttpResponse("Método não permitido nesta página!")

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
    if request.method != "GET":
        return HttpResponse("Método não permitido nesta página!")

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
    if request.method != "GET":
        return HttpResponse("Método não permitido nesta página!")

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


def year(request, year):
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
        "year": year,
        "method": "year",
    }

    r = requests.get(f'http://127.0.0.1:8000/api/posts?method=year&year={year}&page=1').json()

    if not r.get("status"):
        response["posts"] = r

    return render(request, "posts.html", response)


def month(request, year, month):
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
        "year": year,
        "month": month,
        "method": "month",
    }

    r = requests.get(f'http://127.0.0.1:8000/api/posts?method=month&year={year}&month={month}&page=1').json()

    if not r.get("status"):
        response["posts"] = r

    return render(request, "posts.html", response)


def day(request, year, month, day):
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
        "year": year,
        "month": month,
        "day": day,
        "method": "day",
    }

    r = requests.get(f'http://127.0.0.1:8000/api/posts?method=day&year={year}&month={month}&day={day}&page=1').json()

    if not r.get("status"):
        response["posts"] = r

    return render(request, "posts.html", response)


def category(request, category):
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
        "cat": category,
        "method": "category",
    }

    r = requests.get(f'http://127.0.0.1:8000/api/posts?method=category&category={category}&page=1').json()

    if not r.get("status"):
        response["posts"] = r

    return render(request, "posts.html", response)


def author(request, author):
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
        "author": author,
        "method": "author",
    }

    r = requests.get(f'http://127.0.0.1:8000/api/posts?method=author&author={author}&page=1').json()

    if not r.get("status"):
        response["posts"] = r

    return render(request, "posts.html", response)
