async function signIn(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    const name = document.getElementById('name').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://your-api-endpoint/login', {
            method: 'GET',
            headers: {
                'Authorization': 'Basic ' + btoa(name + ':' + password)
            }
        });

        if (response.status === 200) {
            // Successful login, you can redirect or perform other actions here
            alert('Login successful');
        } else {
            // Handle authentication failure
            alert('Login failed. Invalid name or password.');
        }
    } catch (error) {
        console.error('Error during sign-in:', error);
        alert('Error during sign-in. Please try again.');
    }
}
