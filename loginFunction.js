document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const createUserForm = document.getElementById('createUserForm');
    const forgotPasswordForm = document.getElementById('forgotPasswordForm');

    // Toggle to Create User Form
    document.getElementById('createUserBtn').addEventListener('click', function() {
        loginForm.style.display = 'none';
        createUserForm.style.display = 'block';
    });

    // Toggle to Forgot Password Form
    document.getElementById('forgotPasswordBtn').addEventListener('click', function() {
        loginForm.style.display = 'none';
        forgotPasswordForm.style.display = 'block';
    });
});
