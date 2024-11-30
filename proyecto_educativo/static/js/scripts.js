// Example: Alert when a user clicks a button
document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll("button");
    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            alert("Button clicked!");
        });
    });
});