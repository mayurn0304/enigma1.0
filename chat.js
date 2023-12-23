const chatHistoryElement = document.getElementById('chat-history');
const userMessageInput = document.getElementById('user-message');

function sendMessage() {
  const userMessage = userMessageInput.value.trim();

  if (userMessage === '') return;

  appendMessage('You', userMessage);
  processUserMessage(userMessage);
  userMessageInput.value = '';
}

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatHistoryElement.appendChild(messageElement);
  
    // Scroll to the bottom of the chat history
    chatHistoryElement.scrollTop = chatHistoryElement.scrollHeight;
  
    console.log(`Message appended: ${sender} - ${message}`);
  }
  

function processUserMessage(userMessage) {
    // Simple introductory talk
    if (userMessage.toLowerCase().includes('hello') || userMessage.toLowerCase().includes('hi')) {
      const response = 'Hello! I am your online tutoring assistant. How can I help you today?';
      appendMessage('Chatbot', response);
      return;
    }
  
    // Fetch information about assignments
    if (userMessage.toLowerCase().includes('assignment')) {
      // Simulate fetching assignment data from the server
      fetchAssignmentsDataFromServer()
        .then(assignments => {
          const response = getAssignmentInfo(assignments);
          appendMessage('Chatbot', response);
        })
        .catch(error => {
          console.error('assignment-1', error);
          const errorMessage = 'assignment1 submission date is on 5th jan 2024., is there anything else which i can help you with.';
          appendMessage('Chatbot', errorMessage);
        });
      return;
    }
  
    // NLP for class-related queries
    if (processClassQueries(userMessage)) {
      return; // Exit the function if a class-related query was processed
    }
  
    // Respond to common words
    const commonWords = ['schedule', 'attendance', 'report'];
    const lowerCaseMessage = userMessage.toLowerCase();
  
    for (const word of commonWords) {
      if (lowerCaseMessage.includes(word)) {
        const response = `I can help you with ${word}. Is there something specific you'd like to know?`;
        appendMessage('Chatbot', response);
        return;
      }
    }
  
    // Fallback for unrecognized queries
    const response = 'I\'m sorry, I didn\'t understand. Please ask another question.';
    appendMessage('Chatbot', response);
  }
  
  function processClassQueries(userMessage) {
    // Process user message based on NLP for class-related queries
    const lowerCaseMessage = userMessage.toLowerCase();
  
    // Check for specific keywords
    if (lowerCaseMessage.includes('timetable') || lowerCaseMessage.includes('schedule')) {
      // Simulate fetching and displaying the class timetable (replace with actual logic)
      const timetableResponse = 'Here is your class timetable:\nMonday: 9:00 AM - 2:00pm \nTuesday: 9:00 AM - 2:00pm\nwednesday: 9:00 AM - 2:00pm\nthursday: 9:00 AM - 2:00pm\nfriday: 9:00 AM - 2:00pm\nsaturday: 9:00 AM - 12:00 PM';
      appendMessage('Chatbot', timetableResponse);
      return true; // Indicate that a class-related query was processed
    } else if (lowerCaseMessage.includes('cancel class')) {
      // Simulate canceling a class (replace with actual logic)
      const cancelResponse = 'Your class has been canceled. Please check for updates.';
      appendMessage('Chatbot', cancelResponse);
      return true; // Indicate that a class-related query was processed
    } else if (lowerCaseMessage.includes('obtain class schedule')) {
      // Simulate fetching and displaying the overall class schedule (replace with actual logic)
      const overallScheduleResponse = 'Here is the overall class schedule:\nMath: Monday, Wednesday, Friday\nEnglish: Tuesday, Thursday';
      appendMessage('Chatbot', overallScheduleResponse);
      return true; // Indicate that a class-related query was processed
    }
    // Add more conditions as needed for other class-related queries
  
    return false; // Indicate that no class-related query was processed
  }
  
  

function fetchAssignmentsDataFromServer() {
  // Simulate fetching data from the server (replace with actual API call)
  return new Promise((resolve, reject) => {
    // Assuming the teacher is identified by their account ID (replace with actual authentication)
    const teacherId = 'madhusir';

    // Simulating an API call to fetch assignments for the teacher
    // Replace this with an actual API endpoint for fetching assignments based on the teacher's account
    setTimeout(() => {
      const assignmentsData = {
        assignments: [
          {
            title: 'Dynamic Assignment 1',
            description: 'Complete exercises 1-5',
            submissionDate: '2024-03-05'
          },
          {
            title: 'Dynamic Assignment 2',
            description: 'Write a short essay on a given topic',
            submissionDate: '2024-03-15'
          }
          // Add more dynamic assignments as needed
        ]
      };
      resolve(assignmentsData);
    }, 1000); // Simulate a delay for the API call
  });
}

function getAssignmentInfo(assignments) {
  if (assignments && assignments.assignments.length > 0) {
    const assignmentList = assignments.assignments.map(assignment => {
      return `${assignment.title}: ${assignment.description}. Submission Date: ${assignment.submissionDate}`;
    });
    return `Here are your assignments:\n${assignmentList.join('\n')}`;
  } else {
    return 'No assignments available at the moment.';
  }
}
