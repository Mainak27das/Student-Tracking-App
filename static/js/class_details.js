
// button toggle animation
document.querySelector('#exploreClassesBtn').addEventListener('click', function () {
    var buttons = document.querySelectorAll('#exploreIcons .social-btn');
    buttons.forEach(function (button, index) {
        button.style.animationDelay = (index * 0.2) + 's'; // Stagger delay by 0.2s for each button
    });
});

// -----------
