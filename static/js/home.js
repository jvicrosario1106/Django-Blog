var modalBtn = document.querySelector(".modal-btn");
var newsLetter = document.querySelector(".newsletter")
var modalClose = document.querySelector(".fa-window-close");
var btnSubmit = document.querySelector(".news-submit");
var emailInput = document.querySelector(".email");
const forms = document.querySelector("#form");

emailInput.value = '';

forms.addEventListener("submit",function(e){
    e.preventDefault()
   
    if (emailInput.value !== ""){
        
        var r = confirm("Are you sure you want to subcribe?")
       
        if (r == true){
            alert("Click OK to see the results of your subcribing")

        }
        else{
            alert("You Cancelled your subcriptions!")
        }
    }
   else{
        alert("Please Enter your Gmail Account 😀")
   }
    forms.submit();
    forms.reset();
   
},false)



modalBtn.addEventListener("click",function(){
    newsLetter.classList.add("active")
})

modalClose.addEventListener("click",function(){
    newsLetter.classList.remove("active")
})

$(document).ready(function() {
    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.msg-content').fadeOut('slow');
    }, 6000); // <-- time in milliseconds, 1000 =  1 sec
    
});