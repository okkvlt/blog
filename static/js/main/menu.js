import { px, hHeader, hNav } from './global.js';

// MENU

export function open_submenu() {
    $(".submenu").css({
        "opacity": "1",
        "height": px
    });
}

export function close_submenu() {
    $(".submenu").css({
        "opacity": "0",
        "height": "0"
    });
}

// STICKY MENU

export function fix_menu() {
    $("#navbar").addClass("navbar-fixed-top");

    $("#go-top").css({
        "opacity": "1",
        "cursor": "pointer"
    });

    $("body").css("padding-top", hHeader + hNav + 20);

    $("#title-site").css("display", "none");
}

export function drop_menu() {
    $("#navbar").removeClass("navbar-fixed-top");

    $("#go-top").css({
        "opacity": "0",
        "cursor": "default"
    });

    $("body").css("padding-top", "0");

    $("#title-site").css("display", "block");
}

export function logo_hover() {
    $("#site-logo").css({
        "filter": "contrast(125%) grayscale(15%) brightness(105%)"
    })
}

export function logo_dishover() {
    $("#site-logo").css({
        "filter": "contrast(100%) grayscale(0%) brightness(100%)"
    })
}