// Initialize Swiper
var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1, // Display one slide at a time
    spaceBetween: 30, // Add space between slides if needed
    loop: false,
    autoHeight: true, // Adjust height of swiper to match the content
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});
