$(document).foundation();

$(window).on('scroll', Foundation.util.throttle(function(e){
  var scroll = $(document).scrollTop();
  if( scroll > 45) {
    $('body').addClass('scrolled');
  } else {
    $('body').removeClass('scrolled');
  }

}, 300));


$(window).on('resize', Foundation.util.throttle(function(e){
  window.resizeProtocolSidebar();
}, 300));


window.resizeProtocolSidebar = function(){
  var height = $('.sidebar-nav').outerHeight();
  $('.protocol-layout').css('min-height',height + 'px');
};


(function($){

  $(document).ready(function(){

    window.resizeProtocolSidebar();

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


    $('.slide-toggle').each(function(){
      var id = $(this).data('slide-id');
      var panel = $('[data-slide-panel="'+id+'"]');
      var drawer = $('[data-slide-drawer="'+id+'"]');

      $(this).on('click', function(e){
        e.preventDefault();
        panel.toggleClass('closed');
        drawer.toggleClass('closed');
      });
    });

  });

})(jQuery);

$('.row.has-sidebar').css('min-height', $('.sticky').outerHeight() + 'px');
