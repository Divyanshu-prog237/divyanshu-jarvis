import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chaurasiadivyanshu95@gmail.com', 'yourpassword')
    server.sendmail('chaurasiadivyanshu95@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
      if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open instagram' in query:
             webbrowser.open("instagram.com")

        

        elif 'open facebook' in query:
             webbrowser.open("facebook.com") 

        elif 'open Netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'open gmail' in query:
             webbrowser.open("gmail.com")       


        elif 'play music' in query:
            music_dir = 'C:\\Users\\chaur\\OneDrive\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'who is you' in query:
            speak("Sir,I am Jarvis your AI voice Assistant")
        
        elif 'how are you' in query:
            speak("I am fine")
            speak("How are you,Sir")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you fine")

        elif 'who i am' in query:
            speak("If you talk than definitely you are human")

        
        elif 'where is bbd university' in query:
            query = query.replace("where is bbd university", "")
            location = query
            speak("Users ask to locate")
            speak(location)
            webbrowser.open("https://www.google.nl/search?q=where+is+bbdu&ei=Z3GyYZLCLt6Y4-EPo6OY6Ag&ved=0ahUKEwjSkbaX0df0AhVezDgGHaMRBo0Q4dUDCA4&uact=5&oq=where+is+bbdu&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyCggAEEcQsAMQyQMyBwgAELADEEMyBwgAELADEENKBAhBGABQzwZYmBlgshxoAXACeACAAQCIAQCSAQCYAQCgAQHIAQrAAQE&sclient=gws-wiz")

        elif 'quit' in query or 'bye' in query:
            speak("Quiting Sir,Thanks for your time")
            exit()

        elif 'open code' in query:
            codePath = "C:\\Users\\chaur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to divyanshu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chaurasiadivyanshu95@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend divyanshu bhai. I am not able to send this email")    
