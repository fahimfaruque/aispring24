document.addEventListener('DOMContentLoaded', function() {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: false,
        freeMode: true, // This makes the slides "free" and not fixed to snap positions
        // Removed navigation and pagination
    });
});
