// CENTER_BANNER

export function center_banner() {
    $("#banner").css({
        "display": "flex",
        "justify-content": "center"
    });
    $(".nav-item").css("width", "100%");
    $(".submenu").css("width", "100%");
}

export function drop_banner() {
    $("#banner").css({
        "display": "",
        "justify-content": ""
    });
    $(".nav-item").css("width", "125px");
    $(".submenu").css("width", "150px");
}