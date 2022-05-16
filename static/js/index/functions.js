// INSERT/DELETE <br>

export function insert_br_xs() {
    let n_br = $(".br-inserted-xs").length;
    if (n_br < 3) {
        $(".insert-br-xs").before("<br class='br-inserted-xs'>");
    }
}

export function delete_br_xs() {
    $(".br-inserted-xs").remove()
}

export function post_hover(x, color_1) {
    let id = $(x).attr("id");

    let icon = "#" + id + "-icon";
    let title = "#" + id + "-title";
    let text = "#" + id + "-text";

    $(icon).css({ "filter": "contrast(145%) brightness(100%)" });
    $(title).css({ "font-weight": "lighter", "color": color_1 });
    $(text).css({ "font-weight": "lighter", "color": "rgb(100, 100, 100)" });
}

export function post_leave(x, color_0) {
    let id = $(x).attr("id");

    let icon = "#" + id + "-icon";
    let title = "#" + id + "-title";
    let text = "#" + id + "-text";

    $(icon).css({ "filter": "contrast(100%) brightness(65%)" });
    $(title).css({ "font-weight": "", "color": color_0 });
    $(text).css({ "font-weight": "", "color": "rgb(151, 151, 151)" });
}
export function livro_hover(x, color_1) {
    let id = $(x).attr("id");

    let icon = "#" + id + "-livro-icon";
    let title = "#" + id + "-livro-title";
    let autor = "#" + id + "-livro-autor";
    let text = "#" + id + "-livro-text";

    $(icon).css({ "filter": "grayscale(30%) contrast(125%) brightness(100%)" });
    $(title).css({ "font-weight": "lighter", "color": color_1 });
    $(autor).css({ "font-weight": "lighter", "color": color_1 });
    $(text).css({ "font-weight": "lighter", "color": "rgb(100, 100, 100)" });
}

export function livro_leave(x, color_0) {
    let id = $(x).attr("id");

    let icon = "#" + id + "-livro-icon";
    let title = "#" + id + "-livro-title";
    let autor = "#" + id + "-livro-autor";
    let text = "#" + id + "-livro-text";

    $(icon).css({ "filter": "grayscale(0%) contrast(100%) brightness(65%)" });
    $(title).css({ "font-weight": "", "color": color_0 });
    $(autor).css({ "font-weight": "", "color": color_0 });
    $(text).css({ "font-weight": "", "color": "rgb(151, 151, 151)" });
}

export function button_hover(color_0) {
    $("#see-more").css({
        "background-color": color_0,
        "color": "#fff",
    });
}

export function button_leave(color_0) {
    $("#see-more").css({
        "background-color": "transparent",
        "color": color_0,
    });
}

export function see_more_posts(i, method, categoria, author, y, m, d, key, color_main, color_strong) {
    let methods = {
        "all": 'http://127.0.0.1:8000/api/posts?method=all&page=' + i,
        "category": 'http://127.0.0.1:8000/api/posts?method=category&category=' + categoria + '&page=' + i,
        "author": 'http://127.0.0.1:8000/api/posts?method=author&author=' + author + '&page=' + i,
        "year": 'http://127.0.0.1:8000/api/posts?method=year&year=' + y + '&page=' + i,
        "month": 'http://127.0.0.1:8000/api/posts?method=month&year=' + y + '&month=' + m + '&page=' + i,
        "day": 'http://127.0.0.1:8000/api/posts?method=day&year=' + y + '&month=' + m + '&day=' + d + '&page=' + i,
        "search": 'http://127.0.0.1:8000/api/search?method=posts&key=' + key + '&page=' + i,
    }

    let api = methods[method];

    $.getJSON(api, function (posts) {
        if (posts["status"] != "error") {
            if (posts["more"] != true) {
                $("#see-more").css("display", "none");
            }

            $.each(posts["posts"], function (index, post) {
                let id = post.id;
                let title = post.title;
                let text = post.text;
                let banner = post.banner;
                let year = post.datetime.year;
                let month = post.datetime.month;
                let day = post.datetime.day;
                let author = post.author.username;

                let last = $(".p").last().next();

                let html = `
                    <a class="p" href="/posts/id/` + id + `">
                        <div id="` + id + `" onmouseover="mouse_on_post(this, '` + color_strong + `')" onmouseleave="mouse_leave_post(this, '` + color_main + `')" class="row post">
                            <div class="col-sm-3">
                                <div id="` + id + `-icon" style="background-image: url('` + banner + `');" class="icon-post">
                                </div>
                            </div>
                            <div class="col-sm-9 content-post insert-br-xs">
                                <div class="data-post">` + day + ` / ` + month + ` / ` + year + `</div>
                                <h2 id="` + id + `-title" class="title-post">` + title + `</h2>
                                <div id="` + id + `-text" class="text-post">
                                    ` + text + `
                                </div>
                                <div class="author-post">
                                    Autor: ` + author + `
                                </div>
                `

                if (post.keywords != null) {
                    let keywords = post.keywords;

                    let keys = `
                        <div style="width: 71%; margin-left: 25%; background-color: transparent; text-align: left;" class="author-post">
                            Encontrados: | 
                    `

                    for (let key in keywords) {
                        keys += keywords[key] + ' | ';
                    }

                    keys += `
                        </div>
                    `

                    html += keys;
                }

                html += `
                            </div>
                        </div>
                    </a>
                    <br>
                `

                last.after(html);
            });
        }
    });
}