import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
from gtts import gTTS
import random
import urllib 

r = sr.Recognizer()


def kyoyu_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    kyoyu_speak(audio_string)
    os.remove(audio_file)
    
    
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            kyoyu_speak(ask)
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            kyoyu_speak("Sorry, didn't get that, try to be more clear")
        except sr.RequestError:
            kyoyu_speak('Sorry, my speech service is down')
        return voice_data



def respond(voice_data):
    if 'what is your name' in voice_data:
        kyoyu_speak('My name is Kyoyu ^^')
    if 'what time is it' in voice_data:
        kyoyu_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you need to search, cutie?')
        query = urllib.parse.quote(search)
        url = 'http://google.com/search?q=' + query
        webbrowser.get().open(url)
        kyoyu_speak(f"Here's what I found for {search}, sweetheart:")
    if 'find location' in voice_data:
        location = record_audio('Location of what?')
        query = urllib.parse.quote(location)
        url = 'https://www.google.com/maps/place/' + query
        webbrowser.get().open(url)
        kyoyu_speak(f"Here's the location of {location}:")
    if 'exit' in voice_data:
        kyoyu_speak("Goodbye!")
        exit()

time.sleep(1)
kyoyu_speak("How can I help you, cutie?")

while 1:
    voice_data = record_audio()
    respond(voice_data)
