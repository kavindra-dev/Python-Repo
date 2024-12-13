import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Buddy. How can I assist you?")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return None

    return query


def process_query(query):
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        speak(results)
    elif 'open youtube' in query.lower():
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query.lower():
        webbrowser.open("https://www.google.com")
    elif 'play music' in query.lower():
        music_dir = 'C:\\Music'  # Enter your music directory path
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'time' in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'thank you' in query.lower():
        speak("You're welcome!")
        exit()
    else:
        speak("I'm sorry, I can't help with that.")


if __name__ == "__main__":
    greet()
    while True:
        query = listen()
        if query:
            process_query(query)