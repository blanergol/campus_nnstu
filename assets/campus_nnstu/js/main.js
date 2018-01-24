(function ($) {
    "use strict";


    /*---------------------
     jQuery MeanMenu
     --------------------- */
    jQuery('nav#dropdown').meanmenu();


    /*--
     slick slider
     ------------------------*/
    $('.slider-active').slick({
        centerMode: true,
        dots: true,
        fade: true,
        centerPadding: '0',
        slidesToShow: 1,
        arrows: false,
        responsive: [
            {
                breakpoint: 1100,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 970,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });


    /*---------------------
     countdown
     --------------------- */
    $('[data-countdown]').each(function () {
        var $this = $(this), finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="cdown day">%-D <p>Days</p></span> <span class="cdown hour">%-H <p>Hour</p></span> <span class="cdown minutes">%M <p>Min</p></span class="cdown second"> <span>%S <p>Sec</p></span>'));
        });
    });


    /*----------------------------
     counter js active
     ------------------------------ */
    $('.counter').counterUp({
        delay: 5,
        time: 500
    });


    /*--
     slick slider
     ------------------------*/
    $('.slider-active2').slick({
        centerMode: true,
        dots: true,
        centerPadding: '0',
        slidesToShow: 1,
        arrows: false,
        responsive: [
            {
                breakpoint: 1100,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 970,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });
    /*--
     all-courses
     ------------------------*/
    $('.all-courses').slick({
        centerMode: true,
        dots: true,
        centerPadding: '0',
        slidesToShow: 3,
        arrows: false,
        responsive: [
            {
                breakpoint: 1100,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 970,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    /*--
     slick slider
     ------------------------*/
    $('.slider-active3').slick({
        centerMode: true,
        dots: true,
        centerPadding: '0',
        slidesToShow: 1,
        arrows: false,
        responsive: [
            {
                breakpoint: 1100,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 970,
                settings: {
                    slidesToShow: 1,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });


    /*--------------------------
     scrollUp
     ---------------------------- */
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 200) {
            $("#toTop").fadeIn();
        } else {
            $("#toTop").fadeOut();
        }
    });
    $('#toTop').on('click', function () {
        $("html,body").animate({
            scrollTop: 0
        }, 500)
    });

    /*----------------------------
     sticky active
     ------------------------------ */
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 245) {
            $('.stick-h2').removeClass('stick');
        } else {
            $('.stick-h2').addClass('stick');
        }
    });


    /*************************
     tooltip
     *************************/
    $('[data-toggle="tooltip"]').tooltip();


})(jQuery);
