var labels = document.querySelectorAll('label');

labels.forEach(function(label) {
  label.addEventListener('mouseover', function() {
    this.style.color = getRandomColor();
  });

  label.addEventListener('mouseout', function() {
    this.style.color = '#000'; // Change it back to the default color
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