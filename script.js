// Toggle Login Popup
const userIcon = document.getElementById('user-icon');
const loginPopup = document.getElementById('login-popup');

userIcon.addEventListener('click', () => {
    loginPopup.classList.toggle('hidden');
});

// Close popup when clicking outside
document.addEventListener('click', (event) => {
    if (!loginPopup.contains(event.target) && !userIcon.contains(event.target)) {
        loginPopup.classList.add('hidden');
    }
});
document.getElementById("search-toggle").addEventListener("click", function () {
    document.getElementById("search-bar").classList.toggle("hidden")
});