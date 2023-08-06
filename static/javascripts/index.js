new Swiper(".desktop-swiper", {
  slidesPerView: 3,
  spaceBetween: 80,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },
  //   navigation: true,
  grabCursor: true,
  loop: true // to use this option effectively, total slides must be >= slidesPerView * 2
});

// MOBILE SWIPER

new Swiper(".mobile-swiper", {
  slidesPerView: 1,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },
  loop: true
});

// MOBILE END
