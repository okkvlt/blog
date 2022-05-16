import {
    post_hover, post_leave,
    livro_hover, livro_leave,
    button_hover, button_leave,
    see_more_posts
} from './functions.js';

import { loaded_menu, dinamic_menu } from './menu.js';
import { dinamic_recursive, loaded_recursive } from './recursive.js';


const NAV_HEIGHT = 150;
const CURRENT_HEIGHT = window.scrollY;

const MOBILE = 750;
const MIDDLE = 1183;

const WIDTH = $(window).width();
const HEIGHT = $(window).height();

let post_page = 1;

loaded_recursive(WIDTH, MOBILE, MIDDLE);
loaded_menu(CURRENT_HEIGHT, NAV_HEIGHT);

$(window).resize(function () {
    let width = $(window).width();
    let height = window.scrollY;

    dinamic_recursive(width, height, MOBILE, MIDDLE, NAV_HEIGHT);
});

window.addEventListener("scroll", function () {
    let width = $(window).width();
    let height = window.scrollY;

    dinamic_menu(width, height, MOBILE, NAV_HEIGHT);
});

$("#scrolltop").click(function () {
    $("html, body").animate({ scrollTop: "0" });
});

if ($(document).height() <= HEIGHT) {
    $(".footer").css({
        "position": "fixed"
    });
}

window.mouse_on_post = function mouse_on_post(x, color_1) {
    post_hover(x, color_1);
}

window.mouse_leave_post = function mouse_leave_post(x, color_0) {
    post_leave(x, color_0);
}

window.mouse_on_book = function mouse_on_book(x, color_1) {
    livro_hover(x, color_1);
}

window.mouse_leave_book = function mouse_on_book(x, color_0) {
    livro_leave(x, color_0);
}

window.mouse_on_button = function mouse_on_button(color_0) {
    button_hover(color_0);
}

window.mouse_leave_button = function mouse_leave_button(color_0) {
    button_leave(color_0);
}

window.more_posts = function more_posts(method, categoria, author, y, m, d, key, color_main, color_strong) {
    post_page += 1;
    see_more_posts(post_page, method, categoria, author, y, m, d, key, color_main, color_strong);
}