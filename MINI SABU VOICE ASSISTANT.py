import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
c=pyttsx3.init()
try:
    with sr.Microphone() as source:
        print("TELL SOMETHING")
        voice=r.listen(source)
        command=r.recognize_google(voice)
        print(command)
        

        if 'sabu' in command or 'Sabu' in command:
            print("yes tell me i can hear you")
            c.say("yes tell me i can hear you")
            c.runAndWait()
            

except:
    pass

