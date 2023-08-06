new Swiper(".swiper", {
  slidesPerView: 3,
  spaceBetween: 20,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },
  // autoplay: {
  //   delay: 3000,
  //   disableOnInteraction: false
  // }

  // Responsive breakpoints
  breakpoints: {
    // when window width is >= 768px
    768: {
      slidesPerView: 3,
      spaceBetween: 20
    }
  }
});

new Swiper(".desktop-swiper", {
  slidesPerView: 3,
  spaceBetween: 80,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },
  grabCursor: true,
  loop: true
});
