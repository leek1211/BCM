function show_rate(rating) {
  rs = "" + rating;
  if (rs >0)
    $('input:radio[name=rating]').filter('[value='+rs +']').prop('checked',true);
  return true;
}