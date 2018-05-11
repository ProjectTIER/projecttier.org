// Takes a list of tag elements and returns a concatenated string,
// eg. "psychology|economics|history"
function catTags(tagElems) {
  var result = '';
  for(var i=0; i<tagElems.length; i++) {
    if(i>0) {
      result += '|';
    }
    result += $(tagElems[i]).attr('name');
  }
  return result;
}
// Get checkbox states and create URL query
function serializeFilters() {
  // Get all checked tags
  var tags = $('.exercise-filter input[type="checkbox"]:checked');
  // Loop each tag type and build the query string
  var queryString = '?';
  var tagTypes = ['disciplines', 'course-levels', 'protocols'];
  for(var i=0; i<tagTypes.length; i++) {
    var tagType = tagTypes[i];
    var filteredTags = tags.filter('[data-tag="' + tagType + '"]');
    var tagString = catTags(filteredTags);
    if(tagString) {
      if(queryString.length>1) {
        queryString += '&';
      }
      queryString += tagType + '=' + tagString;
    }
  }
  return queryString;
}

// Handle ticking a filter checkbox
$('.exercise-filter input[type="checkbox"]').change(function(e) {
  window.location.href = serializeFilters();
});
