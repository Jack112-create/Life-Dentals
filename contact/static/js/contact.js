const submitBtn = document.getElementById('contact-submit');

function sendMail(e) {
    e.preventDefault();

    const userName = document.getElementById('name');
    const userEmail = document.getElementById('email');
    const userMessage = document.getElementById('message');

    const contactParams = {
        from_name: userName.value,
        from_email: userEmail.value,
        message: userMessage.value
    }

    //  Send email with values from contact form
    emailjs.send("service_covz2ff", "contact_form", contactParams)
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });

    // Reset input values
    userName.value = '';
    userEmail.value = ''
    userMessage.value = '';
    
}

submitBtn.addEventListener('click', (e) => {
    sendMail(e);
})