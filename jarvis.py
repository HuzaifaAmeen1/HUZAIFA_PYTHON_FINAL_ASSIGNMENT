import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak (audio):
     engine.say(audio)
     engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morninng!")

     elif hour>=12 and hour<18:
          speak("Good Afternoon!")

      
     else:
         speak("Good Evening!")
     speak("I am jarvis  sir , how can i assist you today ?")    

def takeCommand():


     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("listning...")
          r.pause_threshold = 1.5
          r.energy_threshold = 3000
          audio = r.listen(source)


     try:
          print("Recognizing...")      
          query = r.recognize_google(audio, language='en_in')
          print(f"User said: {query}")


     except Exception as e: 
          print(e)
          print("say that again please.....")
          return "None"
     
     
     return query
       


if __name__ == "__main__":    
 #wishMe()
 while True:

      Command = takeCommand().lower()
      

      if 'wikipedia' in command:
           speak("Searching Wikipedia...")
           command = command.replace("wikipedia", "")
           results = wikipedia.summary(command, sentences=2)
           speak("According to Wikipedia")
           speak(results)


      elif 'open youtube' in command:
           webbrowser.open("https://www.youtube.com")


      elif 'google' in command:
           webbrowser.open("https://www.google.com")


      elif "Slack" in  command:
           webbrowser.open("https://www.slack.com")
     

      elif 'open VS code' in command:
           codePath = "C:\\Users\\Yousuf Traders\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"   
           os.startfile(codePath)


      elif 'time' in command:
           strtime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the current time is {strtime}")


      elif 'play jokes' in command:
           playjokes = pyjokes.get_joke()
           speak(playjokes)    


      elif 'date' in command:
           strdate = datetime.datetime.now().strftime("%A, %B %d, %Y")
           speak(f"today date is  {strdate}")


      elif 'play song' in command:
           song = webbrowser.open("https://www.youtube.com/watch?v=JiF9anzVqM4&list=RDKzO0iKufUc0&index=5")
           speak("of course {song}")


      elif 'day today' in command:
           day = datetime.datetime.now().strftime("%A")
           speak("today is {day}")  

      elif 'calculator' in command:
           calculator = subprocess.Popen(['calc.exe'])
           open (calculator)     