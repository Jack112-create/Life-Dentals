const config = {
    USER_ID : 'user_TJJYMaTD8WNx5eFtVAj2w',
    TEMPLATE_ID : 'contact_form',
    SERVICE_ID: "service_covz2ff"
};

(function() {
    emailjs.init(config.USER_ID);
})();

const contactForm = document.getElementById('contact-form');
const closeBtn = document.getElementsByClassName('close')[0];

function sendMail(e) {
    console.log(e);
    e.preventDefault();

    const userName = document.getElementById('name');
    const userEmail = document.getElementById('email');
    const userMessage = document.getElementById('message');

    // Sending email with values from each input field.
    emailjs.sendForm(config.SERVICE_ID, config.TEMPLATE_ID, "#contact-form", config.USER_ID)
    .then(function(res) {
        console.log('SUCCESS!', res);
        formModal('success');
    }, function(error) {
        console.log('FAILED...', error);
        formModal('fail');
    });

    // Reset input values
    userName.value = '';
    userEmail.value = ''
    userMessage.value = '';

}

function formModal(formsuccess) {

    const modalDiv = document.getElementById('form-modal');
    const modalMessage = document.getElementsByClassName('modal-message')[0];
    modalDiv.style.display = "block";

    if (formsuccess === 'success') {
        modalMessage.innerText = 'Thanks for getting in touch! We hope to get back to you as soon as possible!'
    } else {
        modalMessage.innerText = 'Oops! looks like there was an error. Try again.'
    }

}

function closeModal() {
    const modalDiv = document.getElementById('form-modal');

    const modalMessage = document.getElementsByClassName('modal-message')[0];
    modalMessage.innerText = ''

    modalDiv.style.display = "none";

}

contactForm.addEventListener('submit', (e) => {
    sendMail(e);
});

closeBtn.addEventListener('click', closeModal);