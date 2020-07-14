const toggleButton = document.querySelector(".toggle-button")
const navLink = document.getElementsByTagName("ul")[0]

toggleButton.addEventListener('click', function(){
    navLink.classList.toggle("active")
})