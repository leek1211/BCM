function show_rate(rating) {
  rs = "" + rating;
  if (rs >0)
    $('input:radio[name=rating]').filter('[value='+rs +']').prop('checked',true);
  return true;
}

function rate_movie(url) {
  
  var tag = $('input:radio:checked');
  if (tag.length == 0) return false;
  else  {
    $.post(url, 
           { rating: tag[0].value}, 
           function(data, status) { 
           });
           hide_modal();
           alert('Rated successfully');

           return false;
  }
}