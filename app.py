from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, static_folder='static')


openai.api_key = 'enter your chatgpt api  key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    response = fetch_chatbot_response(user_input)
    return jsonify({'response': response})

def fetch_chatbot_response(user_input):
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=None,
        frequency_penalty=None,
        presence_penalty=None
    )
    response_text = completion.choices[0].text.strip()
    return response_text

if __name__ == '__main__':
    app.run()


#voice for bonus 
import pyttsx3
engine = pyttsx3.init()

def fetch_chatbot_response(user_input):
    # ... (API request code)
    prompt = f'User: {user_input}\nBot:'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    response_text = response.choices[0].text.strip()
    
    # Speak the response using pyttsx3
    engine.say(response_text)
    engine.runAndWait()
    
    return response_text
