Self-Paced Mentor

The "Self-Paced Mentor" is an interactive Python application built using Kivy, OpenAI, and speech recognition libraries. It acts as a mentor, providing assistance in three different areas: getting help on various topics, conducting mock interviews on user-specified topics, and quick topic revision.

Features

Help on Various Topics:
The application allows users to input their queries or speak them out loud.
It uses OpenAI's GPT-3 engine to generate responses to users' queries and provides real-time text-to-speech feedback using pyttsx3.
Users can either type their doubts or ask their questions verbally using a microphone.

Mock Interview:

Users can request a mock interview on a specific topic, and the mentor generates three questions related to that topic using GPT-3.
The application then records the user's verbal responses to the questions and provides appropriate responses to the user's answers, simulating a mock interview experience.
Quick Topic Revision:

The application allows users to ask for quick revisions on any topic.
Users can provide the topic verbally or by typing it in, and the mentor generates nine key points related to the topic using GPT-3.
The generated points are then presented to the user, aiding in quick topic revision.

Requirements

Python Environment: The application requires Python 3.6 or later to run.
Kivy: The Kivy library must be installed for building the graphical user interface (GUI).
OpenAI GPT-3 API: Obtain the API key for OpenAI GPT-3 and set it in the openai.api_key variable.
Speech Recognition Library: Install the speech_recognition library for audio input from the user's microphone.
Text-to-Speech Library: The pyttsx3 library is used for providing audio feedback to the user.
Google Text-to-Speech: Install the Google Text-to-Speech API for audio feedback. It requires internet access for voice synthesis.

Installation and Usage
Clone the Repository:

Clone this repository to your local machine using git clone.
Install Dependencies
Set API Key:
Obtain the API key for OpenAI GPT-3 and set it in the openai.api_key variable in the code.

Run the Application:
Run the file to start the application.
The GUI will appear, allowing users to interact with the self-paced mentor.

Getting Help:
To get help on various topics, either type your queries in the provided textbox or speak them out loud using a microphone.
The mentor will use GPT-3 to generate responses and provide feedback in both text and speech format.

Mock Interview:
To conduct a mock interview, type or speak the topic you want to be interviewed on.
The mentor will generate three interview questions related to the topic.
Respond verbally to each question, and the mentor will provide appropriate responses, simulating a mock interview experience.

Quick Topic Revision:
To request quick topic revision, type or speak the topic you want to revise.
The mentor will generate nine key points related to the topic for quick revision.