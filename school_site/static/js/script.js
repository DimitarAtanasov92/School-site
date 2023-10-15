var button = document.querySelector('button');

button.addEventListener('mouseover', function() {
  button.style.backgroundColor = getRandomColor();
});

button.addEventListener('mouseout', function() {
  button.style.backgroundColor = '#333';
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