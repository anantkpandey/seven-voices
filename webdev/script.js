// script.js - JavaScript for day1.html
// For King Bran Stark, SevenVoices, April 9, 2025

// Raven counter
let ravensSent = 0;

// On page load, greet the folk
window.onload = function() {
    alert("Welcome to Seven Voices, loyal subjects of King Bran Stark!");
};

// Get elements
const ravenLink = document.getElementById("raven-link");
const ravenCount = document.getElementById("raven-count");

// Add click event to raven link
ravenLink.addEventListener("click", function(event) {
    event.preventDefault(); // Stop default link behavior
    ravensSent++; // Increment tally
    ravenCount.textContent = `Ravens Sent: ${ravensSent}`; // Update display
    console.log(`Raven sent! Total: ${ravensSent}`); // Log for your Hand’s eye
});