// This is a simple script that adds a click event listener to all elements with the class 'my-button'.
// When one of these elements is clicked, a message is logged to the console.

document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.my-button');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            console.log('Button clicked!');
        });
    });
});