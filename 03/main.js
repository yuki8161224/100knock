
const input = document.getElementById("userInput");
const button = document.getElementById("changeBtn");
const msg = document.getElementById("msg");

button.addEventListener("click", function() {
    const value = input.value;
    msg.textContent = value;
});
