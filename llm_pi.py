from guizero import App, TextBox, PushButton, Text
import requests

def get_response():
    # Get the input text from the TextBox
    user_input = input_box.value
    
    # Send the user input to the local Ollama server and get the response
    response = requests.post("http://localhost:5000/complete", json={"prompt": user_input})
    response_data = response.json()
    
    # Display the response in the response box
    response_box.value = response_data['choices'][0]['text']

# Create the GUI app
app = App(title="LLM Communication GUI", width=400, height=300)

# Add a TextBox for user input
input_box = TextBox(app, width="fill", height="fill", multiline=True)

# Add a PushButton to send the input to the LLM
send_button = PushButton(app, text="Send", command=get_response)

# Add a Text widget to display the response from the LLM
response_box = Text(app, text="", width="fill", height="fill", multiline=True)

# Run the GUI app
app.display()
