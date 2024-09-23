console.log('fuck')
// button toggle animation
window.onload=function(){
    console.log('fucku')
    document.querySelector('#exploreClassesBtn').addEventListener('click', function () {
        console.log('fuckme')
        var buttons = document.querySelectorAll('#exploreIcons .social-btn');
    
        buttons.forEach(function (button, index) {
            console.log(button)
            button.style.animationDelay = (index * 0.2) + 's'; // Stagger delay by 0.2s for each button
        });
    });
    
}

// -----------
