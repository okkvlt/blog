
from django.shortcuts import render

from pages.models import *
from pages.utils import utils

# Create your views here.


def index(request):
    try:
        db_config = Config.objects.order_by("-id")[0]

        config = [
            db_config.name,
            db_config.status,
            db_config.year,
            db_config.owner
        ]
    except:
        config = [
            "[Nome do Blog]",
            "[Status do Blog]",
            "[Ano do Blog]",
            "[Dono do Blog]"
        ]

    apresentacao = []

    try:
        db_apresentacao = Apresentacao.objects.order_by("-id")[0]

        apresentacao = [
            db_apresentacao.title,
            db_apresentacao.text,
            db_apresentacao.background
        ]
    except:
        pass

    posts = []

    try:
        db_posts = Posts.objects.order_by("-id")[0:3]

        for post in db_posts:
            posts.append(
                [
                    post.id,
                    post.title,
                    post.text,
                    post.banner,
                    post.date,
                    post.author.first_name
                ]
            )
    except:
        pass

    livros = []

    try:
        db_livros = Livros.objects.order_by("-id")[0:3]

        for livro in db_livros:
            livros.append(
                [
                    livro.id,
                    livro.title,
                    livro.author,
                    livro.banner,
                    livro.descricao
                ]
            )
    except:
        pass

    archive = utils.get_archive(Posts)

    site = {
        "config": config,
        "posts": posts,
        "apresentacao": apresentacao,
        "archive": archive,
        "livros": livros,
    }

    return render(request, "index.html", site)
