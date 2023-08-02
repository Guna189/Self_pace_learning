import os

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
import speech_recognition as sr
import openai
import pyttsx3
import re
import cv2
import threading
import subprocess

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # resp = response.choices[0].text.strip()
    return response.choices[0].text.strip()


Window.size = (800, 600)
Builder.load_file('my12.kv')


openai.api_key = "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"
engine = pyttsx3.init()
# Set voice properties
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('rate', 9999)
engine.setProperty('voice', voices[1].id)  # 0 is the index of the voice you want to use
# Create a recognizer object
r = sr.Recognizer()


class MyMentor(Widget):

    def help(self):
        self.ids.argument.text = "You are eager to know about: "

        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            if self.ids.written_doubt.text != "":
                text = self.ids.written_doubt.text
                print(f"You need: {text}")
                try:
                    engine.say(f"You need: {text}")
                    engine.runAndWait()
                    response = generate_response(text)
                    print(response)
                    self.ids.reply.text = str(response)
                    doubt_text = "You asked about..." + str(text)
                    self.ids.doubt.text = doubt_text
                    engine.say(response)
                    engine.runAndWait()

                except Exception as e:
                    print("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.say("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.runAndWait()
                self.ids.written_doubt.text = ''
            else:
                print("Say something!")
                try:
                    engine.say("Say Something...")
                    engine.runAndWait()
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    doubt_text = "You asked about..." + str(text)
                    self.ids.doubt.text = doubt_text
                    print(f"You said: {text}")
                    engine.say(f"You said: {doubt_text}")
                    engine.runAndWait()
                    response = generate_response(text)
                    print(response)
                    self.ids.reply.text = response
                    engine.say(response)
                    engine.runAndWait()
                except Exception as e:
                    print("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.say("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.runAndWait()
                self.ids.written_doubt.text = ''

    def test(self):
        # recorder = subprocess.Popen("prog25.py 1", shell=True)
        self.ids.argument.text = "Mock Interview on topic"
        with sr.Microphone() as source:
            if self.ids.written_doubt.text != "":
                text = self.ids.written_doubt.text
            else:
                print("Say your topic Name")
                try:
                    engine.say("Say your topic Name...")
                    engine.runAndWait()
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                except Exception as e:
                    print("Unable to listen your speech, try again!!")
                    engine.say("Unable to listen your speech, try again!!")
                    engine.runAndWait()
                    self.test()

            print(f"You need interview on: {text}")
            try:
                engine.say(f"Let's start an mock interview on {text}")
                engine.runAndWait()
                self.ids.doubt.text = "You asked about..." + text
                prompt = "Generate 3 questions about topic " + str(text)
                response = generate_response(prompt)
                ques = response.split('\n')
                print(response)
                reply_text = ""
                for i in ques:
                    reply_text += "Question: "+i+"\n"
                    text=""

                    try:
                        engine.say(i)
                        engine.runAndWait()
                        audio = r.listen(source)
                        text = r.recognize_google(audio)
                    except Exception as e:
                        text="Unable to understand your speech, donot get panic and be louder for next question!"
                        print(text)
                        engine.say(text)
                        engine.runAndWait()

                    reply_text += "Your Response: "+text+"\n\n"
                    text = generate_response(i)
                    reply_text += "Appropriate Response: " + text + "\n\n"
                print("Your mock interview is completed. Now check your responses")
                engine.say("Your mock interview is completed. Now check your responses")
                engine.runAndWait()
                self.ids.reply.text = reply_text
                self.ids.argument = ""
            except Exception as e:
                print("Sorry!!, faced an error" + str(e) + ". Please try again!!")
                engine.say("Sorry!!, faced an error" + str(e) + ". Please try again!!")
                engine.runAndWait()
        # recorder.terminate()

    def revise(self):
        self.ids.argument.text = "You are eager to know about: "

        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            if self.ids.written_doubt.text != "":
                text1 = self.ids.written_doubt.text
                text = "Generate 9 key points on "+self.ids.written_doubt.text
                print(f"You need: {text}")
                try:
                    engine.say(f"You need: {text1}")
                    engine.runAndWait()
                    response = generate_response(text)
                    print(response)
                    self.ids.reply.text = str(response)
                    doubt_text = "Quick Revision on..." + str(text1)
                    self.ids.doubt.text = doubt_text
                    engine.say(response)
                    engine.runAndWait()

                except Exception as e:
                    print("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.say("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.runAndWait()
                self.ids.written_doubt.text = ''
            else:
                print("Say something!")
                try:
                    engine.say("Ask a topic for quick revision...")
                    engine.runAndWait()
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    doubt_text = "Quick Revision on..." + str(text)
                    doubt_text1 = "Generate 9 key points on " + str(text)
                    self.ids.doubt.text = doubt_text
                    print(f"Quick Revision on: {text}")
                    engine.say(doubt_text)
                    engine.runAndWait()
                    response = generate_response(doubt_text1)
                    print(response)
                    self.ids.reply.text = response
                    engine.say(response)
                    engine.runAndWait()
                except Exception as e:
                    print("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.say("Sorry!!, faced an error"+str(e)+". Please try again!!")
                    engine.runAndWait()
                self.ids.written_doubt.text = ''

class MentorApp(App):
    def build(self):
        self.title = "Self-Paced Mentor"
        Window.clearcolor = (1, 1, 1, 1)

        return MyMentor()


if __name__ == '__main__':
    MentorApp().run()
