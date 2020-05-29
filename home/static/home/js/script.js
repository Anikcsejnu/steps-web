(function($) {
    'use strict';

    // Preloader js    
    $(window).on('load', function() {
        $('.preloader').fadeOut(700);
    });

    // Background-images
    $('[data-background]').each(function() {
        $(this).css({
            'background-image': 'url(' + $(this).data('background') + ')'
        });
    });



    // venobox popup
    $(document).ready(function() {
        $('.venobox').venobox();
    });


    // filter
    $(document).ready(function() {
        var containerEl = document.querySelector('.filtr-container');
        var filterizd;
        if (containerEl) {
            filterizd = $('.filtr-container').filterizr({});
        }
        //Active changer
        $('.filter-controls li').on('click', function() {
            $('.filter-controls li').removeClass('active');
            $(this).addClass('active');
        });
    });




    // Aos js
    AOS.init({
        once: true
    });


    $('.carousel').carousel({
        interval: 2000
    })

})(jQuery);