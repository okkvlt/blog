// INSERT <br>

export function insert_br_md() {
    let n_br = $(".br-inserted-md").length;
    if (n_br < 1) {
        $(".insert-br-md").before("<br class='br-inserted-md'>");
    }
}

export function delete_br_md() {
    $(".br-inserted-md").remove()
}