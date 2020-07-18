var modalBtn = document.querySelector(".modal-btn");
var newsLetter = document.querySelector(".newsletter")
var modalClose = document.querySelector(".fa-window-close");
var btnSubmit = document.querySelector(".news-submit");
var emailInput = document.querySelector(".email")
emailInput.value = '';
const forms = document.querySelector("#form")
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
})



modalBtn.addEventListener("click",function(){
    newsLetter.classList.add("active")
})

modalClose.addEventListener("click",function(){
    newsLetter.classList.remove("active")
})

