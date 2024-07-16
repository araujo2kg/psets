window.addEventListener('DOMContentLoaded', function(event){
    fetch('header.html')
    .then(response => response.text())
    .then(data => document.querySelector('header').innerHTML = data)
    // this syntax is just a concise way to create an anonymous function
    // .then(function(response){return response.text();}) would do the same thing.
    // document.querySelector('fo... does not need to be between curly braces because it is a one liner
    .then(function(){
        let page_url = window.location.pathname.slice(1);
        let nav_buttons = document.querySelectorAll('nav a');

        nav_buttons.forEach(function(button){
            let button_href = button.getAttribute('href');
            if (page_url == 'swimming.html' || page_url == 'yoga.html' || page_url == 'martialarts.html'){
                    document.getElementById('dropdown-services').classList.add('highlight-current-page');
                }
             if (button_href == page_url){
                button.classList.add('highlight-current-page');
             }
        });
    });

    fetch('footer.html')
    .then(response => response.text())
    .then(data => document.querySelector('footer').innerHTML = data);
    // all the variables are arbitrary named, they just use the return value of the previous operation
});
