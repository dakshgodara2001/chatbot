import openai
import speech_recognition as sr
import nltk
import tkinter as tk
import pyttsx3
from flask import Flask, request, render_template


nltk.download('punkt')
# Initialize OpenAI API key
openai.api_key = "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"

# Initialize Flask app
app = Flask(__name__)

# Function to get response from OpenAI API
def get_response(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="User: " + text + "\nBot: ",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

# Function to handle user input and get response
def handle_input(text):
    response = get_response(text)
    return response

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Handle user input
@app.route("/get", methods=["GET", "POST"])
def get_bot_response():
    user_input = request.args.get("text")
    response = handle_input(user_input)
    return response

# Run Flask app
if __name__ == "__main__":
    app.run()
