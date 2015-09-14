
function get_movie_modal(movie_id) {
  show_modal();
  $.ajax({
    type:'GET',
    url: 'movie/'+movie_id,
    success: function(data) {
      $('#movie-info-modal-body').html(data);
    }
  });
};

function show_modal() {
  $('#movie-info-modal').modal('show');
}

function hide_modal() {
  $('#movie-info-modal').modal('hide');
}

$(document).ajaxStart(function() {
  $('#movie-info-modal-body').html("Loading...");
});

