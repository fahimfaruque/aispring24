document.addEventListener('DOMContentLoaded', function() {
    // Initialize Swiper
    var swiper = new Swiper('.swiper-container', {
        loop: false,
        autoHeight: true,
        observer: true,
        observeParents: true,
    });

    // Function to filter slides
    function filterSlides(score) {
        swiper.slides.forEach(function(slide, index) {
            const slideScore = slide.dataset.score;
            if (score === 'all' || slideScore === score) {
                swiper.slideTo(index);
                swiper.slides[index].style.display = '';
            } else {
                swiper.slides[index].style.display = 'none';
            }
        });
        swiper.update(); // Update Swiper after changes
    }

    // Attach event listeners to filter buttons
    document.querySelectorAll('.filter-button').forEach(button => {
        button.addEventListener('click', function() {
            const score = this.getAttribute('data-score');
            filterSlides(score);
        });
    });
});
