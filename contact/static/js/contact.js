(function() {
    emailjs.init("user_TJJYMaTD8WNx5eFtVAj2w");
})();

const contactForm = document.getElementById('contact-form');

function sendMail(e) {
    console.log(e);
    e.preventDefault();

    const userName = document.getElementById('name');
    const userEmail = document.getElementById('email');
    const userMessage = document.getElementById('message');

    // Sending email with values from each input field.
    emailjs.sendForm("service_covz2ff", "contact_form", "#contact-form", "user_TJJYMaTD8WNx5eFtVAj2w")
    .then(function(res) {
        console.log('SUCCESS!', res);
    }, function(error) {
        console.log('FAILED...', error);
    });

    // Reset input values
    userName.value = '';
    userEmail.value = ''
    userMessage.value = '';

}

contactForm.addEventListener('submit', (e) => {
    sendMail(e);
});