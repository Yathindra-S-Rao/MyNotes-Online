// function to toggle the favorite or star the note
function set_note_favorite() {
    let favorite = document.querySelector('#noteFavorite');

    if (favorite.className == "far fa-star text-warning") {
        favorite.setAttribute('value', "True");
        favorite.setAttribute('class', 'fas fa-star text-warning');
    }
    else if (favorite.className == "fas fa-star text-warning") {
        favorite.setAttribute('value', "False");
        favorite.setAttribute('class', 'far fa-star text-warning');
    }
    else {
        favorite.setAttribute('value', "False");
        favorite.setAttribute('class', 'far fa-star text-warning');
    }
}

$(document).on('click', '.confirm-delete', function () {
  $("#DeleteConfirmModal").attr("caller-id", $(this).attr("data-object-id"));
});

$(document).on('click', '.confirmDeleteButtonModel', function () {
  var caller = $(".confirmDeleteButtonModel").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});
