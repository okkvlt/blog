from pages.models import *


class Utils:
    def check(self, request, methods_params: dict):
        if request.method != "GET":
            r = {
                "status": "error",
                "info": "method not allowed!"
            }
            return r

        if len(request.GET) == 0:
            r = {
                "status": "error",
                "info": "arguments missing!",
                "methods": methods_params
            }
            return r

        if not "method" in request.GET:
            r = {
                "status": "error",
                "info": "param 'method' is necessary!"
            }
            return r

        if request.GET["method"] not in methods_params.keys():
            r = {
                "status": "error",
                "info": f'method ({request.GET["method"]}) not found!'
            }
            return r

        for arg in methods_params[request.GET["method"]]:
            if not arg in request.GET:
                r = {
                    "status": "error",
                    "info": "insuficient params!",
                    "required params": methods_params[request.GET["method"]]
                }
                return r

        return None

    def posts(self, word):
        posts = Posts.objects.filter

        return [
            posts(title__contains=word).order_by("-id"),
            posts(text__contains=word).order_by("-id")
        ]

    def books(self, word):
        livros = Livros.objects.filter

        return [
            livros(title__contains=word).order_by("-id"),
            livros(author__contains=word).order_by("-id"),
            livros(descricao__contains=word).order_by("-id")
        ]

    def search(self, key: str, method: str, page: int or None):
        if not key:
            return

        methods = {
            "posts": self.posts,
            "books": self.books
        }

        if not method in methods.keys():
            return

        response = {}

        for word in key.split():
            querys = methods[method](word)

            for query in querys:
                for r in query:
                    if not r.id in response.keys():
                        response[r.id] = r.as_dict()

                    if not "keywords" in response[r.id].keys():
                        response[r.id]["keywords"] = [word]
                    else:
                        if not word in response[r.id]["keywords"]:
                            response[r.id]["keywords"].append(word)

        if page:
            items_page = {}

            start = (page - 1) * 5
            end = start + 5

            keys = list(response)[start:end]

            for x in response:
                if x in keys:
                    items_page[x] = response[x]

            if len(list(response)[end:end+5]) != 0:
                items_page["more_posts"] = True

            return items_page

        return response
