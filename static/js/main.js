$(window).bind("load", function() {



    $(document).ready(function() {
        'use strict';


        setTimeout(function() {
            $('.loader_bg').fadeToggle();
        }, 2000);



    });

    $(document).ready(function() {
        $('.checkbtn').click(function() {
            $('#active').toggleClass('active')
        });

        $('nav ul li a').click(function(e) {
            $('.checkbtn').trigger('click');
        });


        $(window).scroll(function() {
            if ($(document).scrollTop() > 300) {
                $('nav').addClass('navbg')
            } else {

                $('nav').removeClass('navbg')
            }

        });





        var typed2 = new Typed('#typed2', {
            strings: [
                "Best Way To Maintain Attendance",
                "Quick Login From Anywhere"
            ],
            typeSpeed: 75,
            backSpeed: 15,
            loop: true,
            onComplete: function() {
                $(".typed-cursor").hide();
            }

        });

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();

                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });





    });


});

$(document).ready(function() {
    // Wrap every letter in a span
    var textWrapper = document.querySelector('.ml6 .letters');
    textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

    anime.timeline({ loop: 2 })
        .add({
            targets: '.ml6 .letter',
            translateY: ["1.1em", 0],
            translateZ: 0,
            duration: 750,
            delay: (el, i) => 50 * i,
            autoplay: false,


        });
});