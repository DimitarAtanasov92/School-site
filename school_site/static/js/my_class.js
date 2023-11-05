document.querySelector('h1').addEventListener('click', function() {
    this.style.color = 'red';
});

document.querySelectorAll('h2').forEach(function(element) {
    element.addEventListener('mouseover', function() {
        this.style.fontSize = '24px';
    });
});