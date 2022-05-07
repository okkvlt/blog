// INSERT/DELETE <br>

export function insert_br_sm() {
    let n_br = $(".br-inserted-sm").length;
    if (n_br < 2) {
        $(".insert-br-sm").before("<br class='br-inserted-sm'>");
    }
}

export function delete_br_sm() {
    $(".br-inserted-sm").remove()
}

export function insert_br_md() {
    let n_br = $(".br-inserted-md").length;
    if (n_br < 1) {
        $(".insert-br-md").before("<br class='br-inserted-md'>");
    }
}

export function delete_br_md() {
    $(".br-inserted-md").remove()
}