from pages.models import *


class Utils:
    def get_config(self):
        try:
            db_config = Config.objects.order_by("-id")[0]

            config = [
                db_config.name,
                db_config.status,
                db_config.year,
                db_config.owner,
                db_config.logo
            ]
        except:
            config = [
                "[Nome do Blog]",
                "[Status do Blog]",
                "[Ano do Blog]",
                "[Dono do Blog]",
            ]

        return config

    def get_colors(self):
        try:
            db_colors = Colors.objects.order_by("-id")[0]

            colors = [
                db_colors.main,
                db_colors.strong,
                db_colors.neutral,
                db_colors.lighter
            ]
        except:
            colors = [
                "#87ad93",
                "#526e5b",
                "#cccccc",
                "#e6f8ec"
            ]

        return colors

    def get_posts(self, num=0):
        posts = []

        try:
            if num == 0:
                db_posts = Posts.objects.order_by("-id")
            else:
                db_posts = Posts.objects.order_by("-id")[0:num]

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

        return posts

    def get_books(self, num=0):
        livros = []

        try:
            if num == 0:
                db_livros = Livros.objects.order_by("-id")
            else:
                db_livros = Livros.objects.order_by("-id")[0:num]

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

        return livros

    def get_archives(self):
        if len(Posts.objects.all()) == 0:
            return

        archive = {}

        months_translate = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }

        first_year = Posts.objects.order_by("date")[0].date.year
        last_year = Posts.objects.order_by("-date")[0].date.year

        c = last_year

        while c >= first_year:
            posts_in_year = Posts.objects.filter(date__year=c).order_by("-date")
            n = len(posts_in_year)

            if n == 0:
                c -= 1
                continue

            archive[c] = [n, {}]

            for post in posts_in_year:
                month = post.date.month
                translated_month = months_translate[month]

                if month in archive[c][1].keys():
                    archive[c][1][month][1] += 1
                else:
                    archive[c][1][month] = [translated_month, 1]

            c -= 1

        return archive

    def get_categorys(self):
        categorias = []

        try:
            db_categorias = Categorias.objects.order_by("-id")

            for categoria in db_categorias:
                categorias.append(
                    [
                        categoria.id,
                        categoria.nome
                    ]
                )
        except:
            pass

        return categorias

    def get_apresentation(self):
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

        return apresentacao
