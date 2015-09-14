function doSearch() {
  var searchInput = $('#search-query')[0].value
  window.location.href='/search/'+ searchInput
  return false;
}
