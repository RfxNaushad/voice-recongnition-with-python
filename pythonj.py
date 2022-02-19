import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os

def speck(text):

    engine = pyttsx3.init()

    # setting the speed
    engine.setProperty('rate', 150)

    # setting the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    engine.say(text)
    engine.runAndWait()

def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("recognizing.......")
        query = r.recognize_google(audio, language='en-in')  
        print(query) 
        return query 
    except Exception as e:
        print(e)
        print("sorry say again.")    



if __name__ == "__main__":
    speck("hello sir ! iam your virtual assistant chi..chi . Let me know how can i help you?")
    while True:
        command = takeVoiceCommand().lower()
        if command == "who are you":
            speck("i am chi chi")
        
        elif "boss" in command:
            speck("my chamcha is shykat")

        elif "youtube" in command:
            webbrowser.open("https://www.youtube.com/watch?v=ksdAs4LBRq8")

        elif "google" in command:
            webbrowser.open("https://www.google.com/")
       
        elif "wikipedia" in command:
            speck("searching in wikipedia......")
            command = command.replace("wikipedia","")
            result = wikipedia.summary(command, sentences = 2)
            speck("according to wikipedia")
            print(result)
            speck(result)

        # elif "open code" in command:
        #     os.startfile("C:\Users\Naushad\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\code.exe")
