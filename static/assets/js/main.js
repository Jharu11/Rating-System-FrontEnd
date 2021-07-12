$(function() {
   

   $('.owl-carousel').owlCarousel({
      autoplay:false,
      loop:false,
      autoplayTimeout:2000,
      margin: 10,
      nav:false,
      dots: true,
      responsive:{
          0:{
            items:1
          },
          300:{
            items:1.7
          },
          400:
          {
            items:2
          },
          500:
          {
            items:2.5
          },
          700:{
            items:2.8
          },
          800:{
            items:3
          },
          1000:{
            items:3
          },
          1200:{
            items:5
          }
      }
   })


  $('.hamberger').click(function(){
    $('.side-bar').addClass('activeSidebar');
  });

  $('.closeBtn-sidebar').click(function(){
    $('.side-bar').removeClass('activeSidebar');
  });

  $('.btn-trailer').click(function(){
    $('.trailer-box').addClass('activeTrailer');
    $('body').css('overflow', 'hidden');
  });

  $('.close-trailer').click(function(){
    $('.trailer-box').removeClass('activeTrailer');
    $('#trailer').attr('src', $('iframe').attr('src'));
    $('body').css('overflow', 'auto');
  });

  $('.rate-now').click(function(){
    $('.rating-box').slideToggle(100);
  });

  $('.user-icon').click(function(){
    $('.user-menu').addClass('user-menu-active');
  });
  $('.notification-icon').click(function(){
    $('.notification-area').addClass('notification-menu-active');
  });
  $('.search-icon').click(function(){
    $('.search-area').addClass('search-menu-active');
  });
  
  $('.btn-rating').click(function(){
    $('.ratingbox').addClass('rating-menu-active');
  });
  $(document).mouseup(function(e){
    if($(e.target).closest('.user-icon').length === 0) {
      $('.user-menu').removeClass('user-menu-active');
    }

    if($(e.target).closest('.notification-icon').length === 0) {
      $('.notification-area').removeClass('notification-menu-active');
    }

    if($(e.target).closest('.search-icon').length === 0) {
      $('.search-area').removeClass('search-menu-active');
    }

    if($(e.target).closest('.rate-form').length === 0) {
      $('.ratingbox').removeClass('rating-menu-active');
    }
  })

  
   

});


