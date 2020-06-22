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

    $('.filter-basic').mdbFilter();
    // $(document).ready(function() {
    //     var containerEl = document.querySelector('.filtr-container');
    //     var filterizd;
    //     if (containerEl) {
    //         filterizd = $('.filtr-container').filterizr({});
    //     }
    //     //Active changer
    //     $('.filter-controls li').on('click', function() {
    //         $('.filter-controls li').removeClass('active');
    //         $(this).addClass('active');
    //     });
    // });


})(jQuery);