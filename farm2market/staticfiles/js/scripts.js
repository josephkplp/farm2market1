// static/js/scripts.js

document.addEventListener("DOMContentLoaded", function () {
    // Function to update total price in the cart
    function updateTotalPrice() {
        let total = 0;
        const items = document.querySelectorAll(".cart-item");
        items.forEach(item => {
            const price = parseFloat(item.querySelector(".item-price").innerText);
            const quantity = parseInt(item.querySelector(".item-quantity").value);
            total += price * quantity;
        });
        document.getElementById("total-price").innerText = total.toFixed(2);
    }

    // Add event listeners for quantity changes
    const quantityInputs = document.querySelectorAll(".item-quantity");
    quantityInputs.forEach(input => {
        input.addEventListener("change", updateTotalPrice);
    });

    // Search functionality
    const searchForm = document.getElementById("search-form");
    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent page reload
            const query = document.getElementById("search-input").value;
            // Redirect to search results page (update URL as needed)
            window.location.href = `/search/?query=${encodeURIComponent(query)}`;
        });
    }

    // Form validation before submission
    const registrationForm = document.getElementById("registration-form");
    if (registrationForm) {
        registrationForm.addEventListener("submit", function (event) {
            let isValid = true;
            const username = document.getElementById("id_username").value.trim();
            const email = document.getElementById("id_email").value.trim();
            const password1 = document.getElementById("id_password1").value.trim();
            const password2 = document.getElementById("id_password2").value.trim();

            // Clear previous messages
            document.getElementById("form-message").innerText = '';

            // Simple validation checks
            if (username === "") {
                isValid = false;
                showMessage("Username is required.", "error");
            } else if (email === "" || !validateEmail(email)) {
                isValid = false;
                showMessage("A valid email is required.", "error");
            } else if (password1.length < 6) {
                isValid = false;
                showMessage("Password must be at least 6 characters long.", "error");
            } else if (password1 !== password2) {
                isValid = false;
                showMessage("Passwords do not match.", "error");
            }

            if (!isValid) {
                event.preventDefault(); // Prevent form submission
            }
        });
    }

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Function to display success/error messages
    function showMessage(message, type) {
        const messageBox = document.getElementById("form-message");
        messageBox.innerText = message;
        messageBox.className = type === "error" ? "error-message" : "success-message";
    }
});
