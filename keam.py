import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.setProperty("rate",150)
    engine.setProperty("volume",1.0)
    engine.runAndWait()

def processcommand(c):
    if"open goggle" in c.lower():
        webbrowser.open("https://google.com")
        speak("yes sir, OPENING google")
    elif"open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("yes sir, OPENING INSTAGRAM")
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("yes sir, OPENING facebook")
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("yes sir, OPENING youtube")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        speak("yes sir , playing one chance!!")
     
if __name__ == "__main__":
    speak("initalization of keam!!")

    while True:
        r = sr.Recognizer()
        print("recognizing!!")
        

        try:
            with sr.Microphone() as source:
                print("listening!!")
                audio = r.listen(source,timeout=4,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "keam"):
                speak("YES, sir")
                print("YES, sir")
                with sr.Microphone() as source:
                  print("keam activate....")
                  speak("keam activate....")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)                
                  processcommand(command)
                
                        
        except sr.UnknownValueError:
            print("sir,could not understand the audio!!")
            speak("sir,could not understand the audio!!")

        except Exception as e:
            print(f"error; {0}".format(e))



