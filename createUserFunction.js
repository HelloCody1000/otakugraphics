function createUser() {
    const formData = {
        username: document.getElementById('newUsername').value,
        userid: document.getElementById('userid').value, // Adjust based on your form's input IDs
        password: document.getElementById('newPassword').value,
        email: document.getElementById('newEmail').value,
    };

    fetch('/create_user', { // Adjust this URL to where your Flask app is hosted
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => alert('Success:', data.message))
    .catch((error) => console.error('Error:', error));
}
