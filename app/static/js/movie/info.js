var ajaxCall;

function get_movie_modal(movie_id) {
  if(ajaxCall!=undefined && ajaxCall.readyState==1 )
    ajaxCall.abort();

  $('#movie-info-modal-body').html("Loading...");
  show_modal();

  ajaxCall = $.ajax({
    type:'GET',
    url: '/movie/'+movie_id,
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


