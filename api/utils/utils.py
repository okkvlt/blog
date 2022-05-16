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

        posts_list = []

        for word in key.split():
            querys = methods[method](word)

            for query in querys:
                for r in query:
                    exists = False

                    for i, post in enumerate(posts_list):
                        if post["id"] == r.id:
                            exists = True
                            posicao = i

                    if exists == False:
                        p = r.as_dict()
                        p["keywords"] = [word]
                        posts_list.append(p)

                    if exists == True:
                        if not word in posts_list[posicao]["keywords"]:
                            posts_list[posicao]["keywords"].append(word)

        if page:
            pages = {
                "posts": 5,
                "books": 15
            }

            start = (page - 1) * pages[method]
            end = start + pages[method]

            if posts_list[end:end+5]:
                response["more"] = True
            else:
                response["more"] = False

            posts_list = posts_list[start:end]

        if posts_list:
            response["status"] = "ok"
            response["posts"] = posts_list
        else:
            response["status"] = "error"
            response["info"] = "nothing found!"

        return response
