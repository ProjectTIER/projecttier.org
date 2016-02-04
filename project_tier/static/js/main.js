$(document).foundation();

$(window).on('scroll', Foundation.util.throttle(function(e){
  var scroll = $(document).scrollTop();
  if( scroll > 45) {
    $('body').addClass('scrolled');
  } else {
    $('body').removeClass('scrolled');
  }

}, 300));


(function($){

  $(document).ready(function(){

    /*
    * Component links inside rich text will automatically hightlight any matching component nav items 
    */
    $('.rich-text a').each(function(){
      var href = $(this).attr('href');
      var components = $('.component-nav a[href="'+href+'"]').addClass('highlight');
      $(this).hover(
        function(){
          components.addClass('active');
        }, function(){
          components.removeClass('active');
        });
    });
  });

})(jQuery);