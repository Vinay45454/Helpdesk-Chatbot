// script.js
const chatForm = document.getElementById('chat-form');
const chatBox = document.getElementById('chatbox');

chatForm.addEventListener('submit', handleFormSubmit);

function handleFormSubmit(event) {
  event.preventDefault();
  
  const userInput = document.getElementById('user-input').value;
  appendUserMessage(userInput);
  
  fetch('/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ user_input: userInput })
  })
    .then(response => response.json())
    .then(data => {
      appendBotMessage(data.response);
    })
    .catch(error => {
      console.error('Error:', error);
      appendBotMessage('An error occurred. Please try again.');
    });
  
  document.getElementById('user-input').value = '';
}

function appendUserMessage(message) {
  const userMessageElement = document.createElement('p');
  userMessageElement.classList.add('user-message');
  userMessageElement.innerText = message;
  chatBox.appendChild(userMessageElement);
  
  scrollToBottom();
}

function appendBotMessage(message) {
  const botMessageElement = document.createElement('p');
  botMessageElement.classList.add('bot-message');
  botMessageElement.innerText = message;
  chatBox.appendChild(botMessageElement);
  
  scrollToBottom();
}

function scrollToBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}
