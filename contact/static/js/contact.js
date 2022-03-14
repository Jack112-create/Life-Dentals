function sendMail() {
    const userName = document.getElementById('name').value;
    const userEmail = document.getElementById('email').value;
    const userMessage = document.getElementById('message').value;

    const contactParams = {
        from_name: userName,
        from_email: userEmail,
        message: userMessage
    }

    emailjs.send("service_covz2ff", "contact_form", contactParams)
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });

    console.log('click');

    return False

}