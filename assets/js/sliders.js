var swiper = new Swiper(".heroSlider", {
  autoplay: true,
  autoplayTimeout: 5000,
  slidesPerView: 1,
  spaceBetween: 5,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

var swiper = new Swiper(".product-slider1", {
  slidesPerView: 4,
  spaceBetween: 16,
  sliderPerGroup: 4,
  loop: false,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  rtl: true,
  breakpoints: {
    0: {
      slidesPerView: 1.3,
      spaceBetween: 4,
    },
    400: {
      slidesPerView: 1.4,
      spaceBetween: 6,
    },
    600: {
      slidesPerView: 2.2,
      spaceBetween: 8,
    },
    900: {
      slidesPerView: 3.2,
      spaceBetween: 16,
    },
    1060: {
      slidesPerView: 4,
      spaceBetween: 16,
    },
    1200: {
      slidesPerView: 4.6,
      spaceBetween: 16,
    },
  },
});
////////////////////////off slider
var swiper = new Swiper(".offSlider", {
  autoplay: true,
  autoplayTimeout: 1000,
  spaceBetween: 16,
  loop: true,
  fade: "true",
});


var swiper = new Swiper(".blog-slider", {
  slidesPerView: 4,
  spaceBetween: 16,
  sliderPerGroup: 4,
  loop: false,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  rtl: true,
  breakpoints: {
    0: {
      slidesPerView: 1.3,
      spaceBetween: 4,
    },
    400: {
      slidesPerView: 1.4,
      spaceBetween: 6,
    },
    600: {
      slidesPerView: 2.2,
      spaceBetween: 8,
    },
    900: {
      slidesPerView: 3.2,
      spaceBetween: 16,
    },
    1060: {
      slidesPerView: 4,
      spaceBetween: 16,
    },
    1200: {
      slidesPerView: 3.8,
      spaceBetween: 16,
    },
  },
});

var swiper = new Swiper(".partnerCompany", {
  slidesPerView: 4,
  spaceBetween: 16,
  sliderPerGroup: 4,
  loop: false,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  rtl: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-btn-prev",
    prevEl: ".swiper-btn-next",
  },
  breakpoints: {
    0: {
      slidesPerView: 3.1,
      spaceBetween: 4,
    },
    400: {
      slidesPerView: 4.5,
      spaceBetween: 6,
    },
    600: {
      slidesPerView: 5.7,
      spaceBetween: 8,
    },
    900: {
      slidesPerView: 6.6,
      spaceBetween: 16,
    },
    1060: {
      slidesPerView: 8.2,
      spaceBetween: 16,
    },
    1200: {
      slidesPerView: 9.7,
      spaceBetween: 10,
    },
  },
});