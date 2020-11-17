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

