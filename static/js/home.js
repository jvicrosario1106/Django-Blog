var modalBtn = document.querySelector(".modal-btn");
var newsLetter = document.querySelector(".newsletter")
var modalClose = document.querySelector(".fa-window-close");
var btnSubmit = document.querySelector(".news-submit");
var emailInput = document.querySelector(".email")
emailInput.value = '';
const forms = document.querySelector("#form")
btnSubmit.addEventListener("click",function(e){
    e.preventDefault()
    
    if (emailInput.value !== ""){
        // forms.submit();
        var r = confirm("Are you sure you want to subcribe?")
        if (r == true){
            alert("Congratulations! We will update you about future posts in this website😍")
            forms.submit();
            forms.reset();
        }
        else{
            alert("You Cancelled your subcriptions!")
        }
    }
   else{
        alert("Please Enter your Gmail Account 😀")
   }
   
    
},false)

modalBtn.addEventListener("click",function(){
    newsLetter.classList.add("active")
})

modalClose.addEventListener("click",function(){
    newsLetter.classList.remove("active")
})

