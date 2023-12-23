async function submitForm(event) {
    event.preventDefault(); // Prevent the default form submission
  
    const url = 'http://127.0.0.1:5000/register';
  
    // Assuming you have form elements with the ids 'usernameInput' and 'passwordInput'
    const username = document.getElementById('name').value;
    const password = document.getElementById('password').value;
  
    const data = {
      username: username,
      password: password
    };
  
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
        // You might need to include additional headers, such as authorization headers
      },
      body: JSON.stringify(data)
    };
  
    try {
      const response = await fetch(url, options);
  
      if (response.ok) {
        const responseData = await response.json();
       alert('Registration successful:', responseData);
      } else {
        alert('Registration failed:', response.status, response.statusText);
      }
    } catch (error) {
      alert('Error during registration:', error);
    }
  }
  
  function handleExtraButton1() {
    console.log("Handle Farmer button click");
    // Add additional actions as needed
  }
  
  function handleExtraButton2() {
    console.log("Handle Transport Provider button click");
    // Add additional actions as needed
  }
  
  // Assuming you have buttons with the ids 'extraButton1' and 'extraButton2'
  document.getElementById('extraButton1').addEventListener('click', handleExtraButton1);
  document.getElementById('extraButton2').addEventListener('click', handleExtraButton2);
  
  // Assuming you have a form with the id 'registrationForm'
  document.getElementById('registrationForm').addEventListener('submit', submitForm);
  