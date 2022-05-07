import { insert_br_xs, delete_br_xs } from './functions.js';

import { open_submenu, close_submenu, fix_menu, drop_menu } from '../main/menu.js';
import { center_banner, drop_banner } from '../main/banner.js';
import { insert_br_md, delete_br_md } from '../main/br.js';

const hHeader = 150;

let width = $(window).width();
let icon_post = 189.375;

if (width < 750) {
    $(".submenu").css({
        "transition": "none",
        "box-shadow": "0 0 0",
        "position": "relative",
        "border-radius": "0"
    });

    $(".apresentation-text").css("padding", "0px 0px");

    open_submenu();
    center_banner();
    drop_menu();
} else {
    $(".submenu-hover").hover(open_submenu, close_submenu);
}

if (width < 750) {
    insert_br_xs();
}

if (width < 1183) {
    insert_br_md();
}

if (window.scrollY > hHeader) {
    fix_menu();
} else {
    drop_menu();
}

$(window).resize(function () {
    width = $(window).width();
    if (width < 750) {
        $(".submenu").css({
            "transition": "none",
            "box-shadow": "0 0 0",
            "position": "relative",
            "border-radius": "0"
        });

        $(".apresentation-text").css("padding", "0px 0px");

        $(".submenu-hover").hover(open_submenu, open_submenu);

        open_submenu();
        center_banner();
        drop_menu();
        insert_br_xs();
    } else {
        $(".submenu").css({
            "transition": "all 0.7s",
            "box-shadow": "0 2px 5px rgba(0, 0, 0, 0.35)",
            "position": "absolute",
            "border-radius": "5px"
        });

        $(".apresentation-text").css("padding", "20px 75px");

        $(".submenu-hover").hover(open_submenu, close_submenu);

        close_submenu();
        drop_banner();
        delete_br_xs();

        if (window.scrollY > hHeader) {
            fix_menu();
        } else {
            drop_menu();
        }
    }

    if (width < 1182) {
        insert_br_md();
    } else {
        delete_br_md();
    }
});

window.addEventListener("scroll", function () {
    if (width > 750) {
        if (window.scrollY > hHeader) {
            fix_menu();
        } else {
            drop_menu();
        }
    } else {
        drop_menu();
    }
});

$("#scrolltop").click(function () {
    $("html, body").animate({ scrollTop: "0" });
});

$(".submenu .item").click(function () {
    let pid = $(this).attr("id");
    window.location.href = "/posts/category_" + pid;
});

$(".content-post").css("height", icon_post);

$(".post").hover(function () {
    let id = $(this).attr("id");
    
    let icon = "#" + id + "-icon";
    let title = "#" + id + "-title";
    let text = "#" + id + "-text";

    $(icon).css({"filter": "contrast(145%) brightness(100%)"});
    $(title).css({"font-weight": "lighter", "color": "rgb(80, 80, 80)"});
    $(text).css({"font-weight": "lighter", "color": "rgb(100, 100, 100)"});
}, function () {
    let id = $(this).attr("id");
    
    let icon = "#" + id + "-icon";
    let title = "#" + id + "-title";
    let text = "#" + id + "-text";

    $(icon).css({"filter": "contrast(100%) brightness(65%)"});
    $(title).css({"font-weight": "", "color": "rgb(126, 126, 126)"});
    $(text).css({"font-weight": "", "color": "rgb(151, 151, 151)"});
});

$(".post").click(function () {
    let id = $(this).attr("id");

    window.location.href = "/posts/" + id;
});

$(".livro").click(function () {
    let id = $(this).attr("id");

   window.open("/livros/" + id, "_blank");
})

$(".livro").hover(function () {
    let id = $(this).attr("id");
    
    let icon = "#" + id + "-livro-icon";
    let title = "#" + id + "-livro-title";
    let autor = "#" + id + "-livro-autor";
    let text = "#" + id + "-livro-text";

    $(icon).css({"filter": "grayscale(30%) contrast(125%) brightness(100%)"});
    $(title).css({"font-weight": "lighter", "color": "rgb(80, 80, 80)"});
    $(autor).css({"font-weight": "lighter", "color": "rgb(80, 80, 80)"});
    $(text).css({"font-weight": "lighter", "color": "rgb(100, 100, 100)"});
}, function () {
    let id = $(this).attr("id");
    
    let icon = "#" + id + "-livro-icon";
    let title = "#" + id + "-livro-title";
    let autor = "#" + id + "-livro-autor";
    let text = "#" + id + "-livro-text";

    $(icon).css({"filter": "grayscale(0%) contrast(100%) brightness(65%)"});
    $(title).css({"font-weight": "", "color": "rgb(126, 126, 126)"});
    $(autor).css({"font-weight": "", "color": "rgb(126, 126, 126)"});
    $(text).css({"font-weight": "", "color": "rgb(151, 151, 151)"});
});