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