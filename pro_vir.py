import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.setProperty("rate",150)
    engine.setProperty("volume",1.0)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initalization of jarvis!!")
    
    while True:
        r = sr.Recognizer()
        print("recognizing!!")

        try:
            with sr.Microphone() as source:
              print("listening!!")
              audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            
            if(word.lower() == "jarvis"):
                speak("yess ,sir!!")

            elif(word.lower() == "how are you"):
                   speak("i am fine ,sir")

            elif(word.lower() == "exit"):
                speak("EXITING FROM THE PROGRAM , GOODBYE!!")
                break           
                                                              

            with sr.Microphone() as source:
                 
                   print("jarvis activating!")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)
                   print(f"command resvied: {command}")
                   processcommand(command)
            
            if("HOW are u" in command):
                   speak("i am fine ,sir")

        except Exception as e:
            print("error;{0}".format(e))

        
        
        except sr.RequestError as e:
            # Handle errors from the Google Web Speech API
            print(f"JARVIS error: {e}")
            speak("There was an issue with the speech recognition service.")