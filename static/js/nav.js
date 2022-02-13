const navToggle = document.getElementById('navToggle');
const nav = document.getElementById('nav-links');

navToggle.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
    console.log('click')
})