document.addEventListener('DOMContentLoaded', function() {
    var swiper = new Swiper('.swiper-container', {
        // existing configuration
    });

    // Attach event listener to score filter
    document.getElementById('scoreFilter').addEventListener('change', function() {
        var selectedScore = this.value;
        filterSlides(selectedScore);
    });

    // Modify filterSlides to work with 'all' option
    function filterSlides(score) {
        swiper.slides.forEach(function(slide) {
            const slideScore = slide.dataset.score; // Ensure your slides have a data-score attribute
            if (score === 'all' || slideScore === score) {
                slide.style.display = '';
            } else {
                slide.style.display = 'none';
            }
        });
        swiper.update(); // Important to call this to reinitialize the swiper layout
    }
});
