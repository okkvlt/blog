from pages.models import *
import unidecode


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
                "#a74242",
                "#661515",
                "#cccccc",
                "#f8cfcf"
            ]

        return colors

    def get_posts(self, author=None, category=None, year=None, month=None, day=None, by="id", num=0):
        posts = []

        modes = {
            "id": Posts.objects.order_by("-id"),
            "author": Posts.objects.filter(author__username=author).order_by("-id"),
            "category": Posts.objects.filter(categoria__nome__iexact=category).order_by("-id"),
            "year": Posts.objects.filter(date__year=year).order_by("-date"),
            "month": Posts.objects.filter(date__year=year, date__month=month).order_by("-date"),
            "day": Posts.objects.filter(date__year=year, date__month=month, date__day=day).order_by("-date"),
        }

        try:
            if num == 0:
                db_posts = modes[by]
            else:
                db_posts = modes[by][0:num]

            for post in db_posts:
                posts.append(
                    [
                        post.id,
                        post.title,
                        post.text,
                        post.banner,
                        post.date,
                        post.author.first_name,
                        []
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
                        livro.descricao,
                        livro.file,
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
            "01": "Janeiro",
            "02": "Fevereiro",
            "03": "Março",
            "04": "Abril",
            "05": "Maio",
            "06": "Junho",
            "07": "Julho",
            "08": "Agosto",
            "09": "Setembro",
            "10": "Outubro",
            "11": "Novembro",
            "12": "Dezembro"
        }

        first_year = Posts.objects.order_by("date")[0].date.year
        last_year = Posts.objects.order_by("-date")[0].date.year

        c = last_year

        while c >= first_year:
            posts_in_year = Posts.objects.filter(
                date__year=c).order_by("-date")
            n = len(posts_in_year)

            if n == 0:
                c -= 1
                continue

            archive[c] = [n, {}]

            for post in posts_in_year:
                month = str(post.date.month).zfill(2)
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
                        categoria.nome,
                        unidecode.unidecode(
                            str(categoria.nome).lower().replace(" ", "-"))
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

    def get_about(self):
        try:
            db_about = Sobre.objects.order_by("-id")[0]

            about = [
                db_about.title,
                db_about.text,
            ]
        except:
            about = []

        return about

    def get_post_byid(self, pid):
        try:
            db_post = Posts.objects.get(id=pid)

            post = [
                db_post.title,
                db_post.text,
                db_post.date,
                db_post.categoria,
                db_post.author.first_name,
                db_post.banner,
                db_post.author.username,
                unidecode.unidecode(
                    str(db_post.categoria).lower().replace(" ", "-"))
            ]
        except:
            post = []

        return post

    def get_search(self, results, word, mode):
        for result in mode:
            if result in results.keys():
                if not word in results[result]:
                    results[result].append(word)
            else:
                results[result] = [word]

        return results

    def search_for_posts(self, key):
        words = key.split()

        results = {}
        posts = []

        for word in words:
            titles = Posts.objects.filter(title__contains=word).order_by("-id")
            texts = Posts.objects.filter(text__contains=word).order_by("-id")

            if titles.count() == 0 and texts.count == 0:
                continue

            results = self.get_search(results, word, titles)
            results = self.get_search(results, word, texts)

        for post in results.keys():
            posts.append(
                [
                    post.id,
                    post.title,
                    post.text,
                    post.banner,
                    post.date,
                    post.author.first_name,
                    results[post]
                ]
            )

        return posts
