import pyttsx3 #pip install pyttsx3
import datetime
#import speech_recognition as sr #pip install speech_recognition
import speech-recognition-python as sr#pip install speech-recognition-python
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait

#This is current time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

#This is current time and date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

#This is wish function
def wishme():
    speak("Welcome back Gaurav Sir")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Gaurav Tyagi sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Gaurav Tyagi sir")
    elif hour >= 18 and hour <=24:
        speak("Good evening Gaurav Tyagi sir")
    else:
        speak("Good night Gaurav Tyagi sir")

    speak("How can i help you Gaurav Tyagi Sir")

#This is a take command for speech recognition function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, 'en=US')
        print(query)
    
    except Exception as e:
        print(e)
        speak("say that again please...")

        return "None"

    return query

#This is a send email function
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test")
    server.sendmail("text@gmail.com", to, content)
    server.close()

 #This is a screenshot function
 def screenshot():
     img = pyautogui.screenshot()
     img.save("C:\Users\Gaurav Tyagi\Desktop\python_projects\personal_assistant\ss.png")

#This is a CPU and battery update function
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)

#This is a jokes function
def jokes():
    speak(pyjokes.get_joke())

#This is a main function
if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            quit()

        #This is a wikepedia search function
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence = 2)
            speak(result)

        #This is a send mail function
        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Your email sent successfully...")

            except Exception as e:
                speak(e)
                speak("Unable to sent the email")

        #This is a chrome search function
        elif "Search in chrome" in query:
            speak("What should i search?")   
            chromepath = "C:\Users\Gaurav Tyagi\AppData\Local\Google\Chrome\Application\chrome.exe %s"  
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        #This is a os system(logout,restart) function
        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        #This is a playing song function
        elif "play songs" in query:
            songs_dir = "F:\Gaurav Doc\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        #This is a create file(read,write,open) function
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())

        #This is a screenshot function
        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        #This is a CPU and battery update function
        elif "cpu" in query:
            cpu()

        #This is a jokes function
        elif "joke" in query:
            jokes()