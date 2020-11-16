$(document).ready(function(){
    $('.sidenav').sidenav({edge: "left"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy" ,
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    $('.modal').modal();     
  });

// to automatically remove flash message

setTimeout(function () {
    $(".flashes").fadeOut('slow');
  }, 5000);

// To validate when user will only enter white spaces

const review = document.getElementById("user_review")
const form = document.getElementById("form")
const errorElement = document.getElementById("error")

form.addEventListener("submit", (e) => {
    let message = []
    if (review.value === "" | review.value === null) {
        message.push("Please add your comments")
    }

    if (messages.length > 0 ) {
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
})

