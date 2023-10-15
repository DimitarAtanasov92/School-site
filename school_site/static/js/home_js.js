var navLinks = document.querySelectorAll('nav ul li a');

navLinks.forEach(function(link) {
  link.addEventListener('mouseover', function() {
    this.style.color = getRandomColor();
  });

  link.addEventListener('mouseout', function() {
    this.style.color = '#fff'; // Change it back to the default color
  });
});

// Function to generate random color
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}