# AUX FUNCTIONS

def get_archive(Posts):
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
