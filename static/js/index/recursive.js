import { insert_br_xs, delete_br_xs } from './functions.js';
import { open_submenu, close_submenu, fix_menu, drop_menu } from './menu.js';
import { center_banner, drop_banner } from './banner.js';
import { insert_br_md, delete_br_md } from './br.js';


export function loaded_recursive(WIDTH, MOBILE, MIDDLE) {
    if (WIDTH < MOBILE) {
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
        insert_br_xs();
    } else {
        $(".submenu-hover").hover(open_submenu, close_submenu);
    }

    if (WIDTH < MIDDLE) {
        insert_br_md();
    }
}

export function dinamic_recursive(width, height, MOBILE, MIDDLE, NAV_HEIGHT) {
    if (width < MOBILE) {
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

        if (height > NAV_HEIGHT) {
            fix_menu();
        } else {
            drop_menu();
        }
    }

    if (width < MIDDLE) {
        insert_br_md();
    } else {
        delete_br_md();
    }
}