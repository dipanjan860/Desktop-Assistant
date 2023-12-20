import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import datetime
from datetime import date

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet(hour):
    if(hour>=4 and hour<12):
        return "good morning"
    elif(hour>=12 and hour<17):
        return "good afternoon"
    elif(hour>=17 and hour<20):
        return "good evening"
    else:
        return "Hello"


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 400
        r.phrase_threshold = 0.1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry From Friday."


if __name__ == '__main__':
    print("<-------------  Welcome to F.R.I.D.A.Y. AI  ------------->")
    hour = int(datetime.datetime.now().strftime("%H"))
    speak(f"{greet(hour)} sir, I am Friday. How can I help you ?")
    while True:
        print("Listening...")
        query = take_command()
        speak(query)

        sites = [["google", "https://www.google.com"], ["youtube", "https://www.youtube.com"],
                 ["mail", "https://mail.google.com/mail/u/0/#inbox"],
                 ["map", "https://www.google.com/maps/@22.7630932,88.3885198,13z?authuser=0&entry=ttu"],
                 ["meet", "https://meet.google.com/?hs=197&authuser=0"],
                 ["drive", "https://drive.google.com/drive/u/0/my-drive"],
                 ["wikipedia", "https://www.wikipedia.com"],
                 ["facebook", "https://www.facebook.com/?ref=homescreenpwa"],
                 ["instagram", "https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1"],
                 ["linkedin", "https://www.linkedin.com/feed/"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir.")
                webbrowser.open(site[1])

        apps = [["code", "C:\\Users\\DIPANJAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
                ["word", "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"],
                ["excel", "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"],
                ["powerpoint", "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"],
                ["note", "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"]]
        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                speak(f"Opening {app[0]} sir.")
                os.startfile(app[1])

        if "the time".lower() in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")

        elif "the date".lower() in query.lower():
            date_ = date.today()
            speak(f"Sir, the date is {date_}")

        elif "your name".lower() in query.lower():
            speak("My name if Friday, sir.")

        elif "friday stop".lower() in query.lower():
            speak("Ok sir, see you later.")
            exit()
