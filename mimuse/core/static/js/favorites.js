$(".btn btn-primary").onclick = function() {
    var id = $(this).attr("id");
    $.get(`favorites/update/${id}/`);
};