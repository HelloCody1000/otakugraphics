document.getElementById('forgotPasswordBtn').addEventListener('click', function() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('forgotPasswordForm').style.display = 'block';
});

document.getElementById('createUserBtn').addEventListener('click', function() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('createUserForm').style.display = 'block';
});

document.getElementById('sendResetEmailBtn').addEventListener('click', function() {
    const email = document.getElementById('email').value;
    // Here, add your logic to validate the email and send a reset email
    // This could be an AJAX/fetch request to your backend
});

document.getElementById('newUserForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('newUsername').value;
    const email = document.getElementById('newEmail').value;
    const password = document.getElementById('newPassword').value;
    // Here, add your logic to validate the new user data and create the user
    // This could be an AJAX/fetch request to your backend
});
