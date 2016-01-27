$(document).foundation();

$(window).on('scroll', Foundation.util.throttle(function(e){
  var scroll = $(document).scrollTop();
  if( scroll > 45) {
    $('body').addClass('scrolled');
  } else {
    $('body').removeClass('scrolled');
  }

}, 300));