const testimonials = [
    {
        name: "-(Caitlin)",
        message: "Everybody was extremely kind and made me feel comfortable throughout my entire treatment process."
    },
    // {
    //     name: "-(John)",
    //     message: "The professionals at Life Dentals explained my treatment process very clearly to me. This gave me the confidence to go ahead with my treatment."
    // },
    // {
    //     name: "-(Barry)",
    //     message: "Great customer experience! The team did a great job at giving me my dream smile with no pain involved!"
    // }
]

function createTestimonials() {

    for (let testimonial of testimonials) {
    let testimonialText = document.createElement('p');
    testimonialText.innerText = testimonial.message;
    testimonialText.classList.add("testimonial-text");

    let testimonialPerson = document.createElement('span');
    testimonialPerson.innerText = testimonial.name;
    testimonialPerson.classList.add("testimonial-person");

    let testimonialSection = document.getElementsByClassName('testimonial')[0];
    testimonialSection.appendChild(testimonialText);
    testimonialSection.appendChild(testimonialPerson);
    }

}

createTestimonials()