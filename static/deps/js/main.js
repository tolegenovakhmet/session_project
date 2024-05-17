/* ===    SWIPER CAREGORIES    ===*/  
var swiperCategories = new Swiper(".categories__container", {
    spaceBetween: 10,
    loop: true,

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 4,
          spaceBetween: 40,
        },
        1400: {
          slidesPerView: 6,
          spaceBetween: 24,
        },
      },
  });

var swiperProducts = new Swiper(".new__container", {
    spaceBetween: 10,
    loop: true,

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 4,
          spaceBetween: 40,
        },
        1400: {
          slidesPerView: 4,
          spaceBetween: 24,
        },
      },
  });

const tabs = document.querySelectorAll('[data-target]'),
    tabContent = document.querySelectorAll('[content]');

    tabs.forEach((tab) => {
        tab.addEventListener('click', () => {
            const target = document.querySelector(tab.dataset.target);
            tabContents.forEach((tabContent) =>{
                tabContent.classList.remove('active-tab');
            });
            target.classList.add('active-tab');

            tabs.forEach((tab) =>{
                tab.classList.remove('active-tab');
            });
            tab.classList.add('active-tab');    
        }); 
    });
