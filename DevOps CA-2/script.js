// JavaScript for form validation

window.addEventListener('load', function() {
    document.getElementById('feedbackForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default submission

        // Clear previous errors
        clearErrors();

        let isValid = true;

        // Validate Student Name
        const name = document.getElementById('name').value.trim();
        if (name === '') {
            showError('nameError', 'Student Name should not be empty.');
            isValid = false;
        }

        // Validate Email
        const email = document.getElementById('email').value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showError('emailError', 'Email should be in proper format.');
            isValid = false;
        }

        // Validate Mobile Number
        const mobile = document.getElementById('mobile').value.trim();
        const mobileRegex = /^\d{10}$/; // Assuming 10 digits
        if (!mobileRegex.test(mobile)) {
            showError('mobileError', 'Mobile Number should contain 10 valid digits only.');
            isValid = false;
        }

        // Validate Department
        const department = document.getElementById('department').value;
        if (department === '') {
            showError('departmentError', 'Department should be selected.');
            isValid = false;
        }

        // Validate Gender
        const gender = document.querySelector('input[name="gender"]:checked');
        if (!gender) {
            showError('genderError', 'At least one gender option should be selected.');
            isValid = false;
        }

        // Validate Feedback Comments
        const comments = document.getElementById('comments').value.trim();
        const wordCount = comments.split(/\s+/).filter(word => word.length > 0).length;
        if (wordCount < 10) {
            showError('commentsError', 'Feedback Comments should not be blank and should meet minimum length of 10 words.');
            isValid = false;
        }

        if (isValid) {
            alert('Form submitted successfully!');
            // Here you can send the data to a server or handle submission
        }
    });
});

function showError(elementId, message) {
    document.getElementById(elementId).textContent = message;
    document.getElementById(elementId).style.display = 'block';
}

function clearErrors() {
    const errors = document.querySelectorAll('.error');
    errors.forEach(error => {
        error.textContent = '';
        error.style.display = 'none';
    });
}

// Reset button functionality (optional, since reset is built-in)
document.getElementById('resetBtn').addEventListener('click', function() {
    clearErrors();
});