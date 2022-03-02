let testimonials = document.getElementsByClassName('testimonial-content');
const prev = document.getElementById('prev');
const next = document.getElementById('next');
const totalTestimonials = testimonials.length;
let index = 0;
console.log(testimonials);

function nextTestimonial(direction) {
    if(direction == 'next') {
      index++;
      if(index == totalTestimonials) {
        index = 0;
      }
    } else {
      if(index == 0) {
        index = totalTestimonials - 1;
      } else {
        index--;
      }
    }
  
    for(let i = 0; i < testimonials.length; i++) {
      testimonials[i].classList.remove('show-testimonial');
    }
    testimonials[index].classList.add('show-testimonial');
}

prev.addEventListener('click', () => {
  nextTestimonial('next');
})

next.addEventListener('click', () => {
  nextTestimonial('prev');
})
