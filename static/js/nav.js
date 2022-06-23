const navToggle = document.getElementById('navToggle');
const nav = document.getElementById('nav-links');

navToggle.addEventListener('click', () => {
    // Toggle navbar to open and close
    nav.classList.toggle('nav-open');
});