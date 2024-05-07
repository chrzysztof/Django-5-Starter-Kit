(function () {
    console.log('Main script is loaded...')
}());

document.addEventListener("DOMContentLoaded", function() {
    var formFields = document.querySelectorAll("input[type='email'], input[type='text'], input[type='tel'], input[type='password']");
  
    formFields.forEach(function(field) {
      field.classList.add("form-control");
    });
  });
