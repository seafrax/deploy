// script.js

document.addEventListener('DOMContentLoaded', function() {
  // Get the form element
  var form = document.querySelector('form');

  // Add event listener to the form submission
  form.addEventListener('submit', function(event) {
      // Get the file input element
      var fileInput = document.querySelector('input[type="file"]');

      // Check if a file has been selected
      if (!fileInput.files || fileInput.files.length === 0) {
          // Prevent form submission if no file is selected
          event.preventDefault();
          alert('Please select an image file to upload.');
      }
  });
});
