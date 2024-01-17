function changeFavorite() {
    pk = $(this).attr("data-pk");
      $.ajax({
                 type: 'POST',
                 url: `favorites/update/${data-pk}/`,
                 data: pk,
                 processData: false,
                 contentType: false,
                 success: function(json) {
                     alert(json);
                 }
             }) 
};