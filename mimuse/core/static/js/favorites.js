$(".btn btn-primary").onclick = function() {
    var id = $(this).attr("data-pk");
    $.get(`favorites/update/${id}/`);
};