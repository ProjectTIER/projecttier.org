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

  // Generate table of contents menu
  function createTableOfContents( parent, placeholder, options ) {

    // Options defaults
    if ( typeof options == 'undefined' ) var options = {};
    if ( !( 'normalize' in options ) ) options.normalize = true;

    // Slugify
    function slugify( text ){
      return text.toString().toLowerCase()
        .replace( /\s+/g, '-' )           // Replace spaces with -
        .replace( /[^\w\-]+/g, '' )       // Remove all non-word chars
        .replace( /\-\-+/g, '-' )         // Replace multiple - with single -
        .replace( /^-+/, '' )             // Trim - from start of text
        .replace( /-+$/, '' );            // Trim - from end of text
    }

    // Return the depth of a H1-H6 as a number
    function getHeaderDepth( hElement ) {
      return parseInt($( hElement ).prop( 'tagName' )[1]);
    }

    // Set variables
    var headers = $( parent ).find( 'h3,h4,h5,h6' );
    if ( headers.length == 0 ) return;
    var prevDepth = 0;
    var prevOrigDepth = 0;
    var menuHTML = '';
    var count = 0;
    var offset = getHeaderDepth( headers[0] );

    $( headers ).each( function(){

      // Menu item object
      var menuItem = {
        'title': $( this ).text(),
        'slug': slugify($( this ).text()),
        'depth': getHeaderDepth($( this )),
        'element': $( this )
      }

      // Apply offset
      menuItem.depth = menuItem.depth - offset + 1;
      if ( menuItem.depth < 1 ) menuItem.depth = 1;

      // Change in depth from previous header
      var depthDiff = menuItem.depth - prevDepth;

      // Normalize list
      var _prevOrigDepth = prevOrigDepth;
      prevOrigDepth = menuItem.depth;
      if ( options.normalize ) {
        if ( menuItem.depth == _prevOrigDepth ) {
          menuItem.depth = prevDepth;
          depthDiff = 0;
        } else if ( depthDiff > 1 ) {
          menuItem.depth = menuItem.depth - depthDiff + 1;
          depthDiff = 1;
        }
      }

      // Constrain depth
      if ( ( 'maxDepth' in options ) && menuItem.depth > options.maxDepth ) {
        return;
      }

      // Indentation
      if ( depthDiff > 0 ) {
        for( var i = 0; i < depthDiff; i++ ) {
          menuHTML += '<ul><li>';
        }
      }
      // Deindentation
      else if ( depthDiff < 0 ) {
        for( var i = 0; i < Math.abs( depthDiff ); i++ ) {
          menuHTML += '</li></ul>';
        }
      }
      // No indentation change
      else if ( depthDiff == 0 ) {
        menuHTML += '</li><li>';
      }

      // Menu item
      menuHTML += '<a href="#' + menuItem.slug + '">' + menuItem.title + '</a>';

      menuItem.element.html('<a name="' + menuItem.slug + '"></a>' + menuItem.element.html());

      // Save for next iteration
      prevDepth = menuItem.depth;
      count++;

    });

    // Write HTML
    $( placeholder ).html( menuHTML );

    // Return data about the process
    return {
      'headers': headers,
      'count': count
    };

  }

  var menu_meta = createTableOfContents( '.page-content', '#table-of-contents', {'maxDepth': 2} );
  var menu = $( '.article-nav' );
  // Hide menu if there aren't enough
  if ( typeof menu_meta == 'undefined' ) {
    menu.hide();
  } else {
    menu.find('ul').first().addClass('vertical menu');
  }

})(jQuery);
