// Function to handle user login
function loginUser(username, password) {
    fetch('https://your-api-endpoint.com/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        if(data.authenticated) {
            console.log('Login Successful');
            // Redirect user or update UI accordingly
        } else {
            console.log('Login Failed: ' + data.message);
            // Show error to the user
        }
    })
    .catch(error => console.error('Error:', error));
}

// Attach this function to your form's submit event
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    loginUser(username, password);
});
