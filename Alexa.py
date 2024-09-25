
# packages for Alexa
# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio
# if not recognize then pip install --upgrade setuptools
# pip install pywhatkit
# pip install wikipedia





import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


class SiriDetectedException(Exception):
    pass

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  # Speed of speech (default: 200)
engine.setProperty('volume', 3.5)
engine.say('....Hi, I am Alexa. ....What I can do for you?')
engine.runAndWait()
def talk(text):

   engine.say(text)
   engine.runAndWait()
   print(text)


def input():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            listener.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=5, phrase_time_limit=5) # Set time limits
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
                talk(command)
            command =command.lower()
            if 'hey siri' in command:
                raise SiriDetectedException("Use Alexa word to Run..")
                print(command)
            return command

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")

    except sr.RequestError:
        print("Internet connection error. Please check your connection.")
    except Exception as e:
        print(f"Error: {e}")
def run_alexa():
    command = input()
    if command is not None:
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk('playing ' + song)
            try:
                pywhatkit.playonyt(song)
                print(f"Playing {song} on YouTube")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M:%S %p')
            print(time)
            talk('The current time is ' + time)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            print(date)
            talk('Todays date is' +date)
        elif 'who' in command:
            person = command.replace('who','')
            info = wikipedia.summary(person,1)
            print(info)
            talk(info)
        elif 'tell me about' in command:
            person1 = command.replace('tell me about','')
            info1 = wikipedia.summary(person1,3)
            print(info1)
            talk(info1)
        elif 'exit' in command:
            talk('Okay...')
            exit()

        else:
            print(f"Command not recognized: {command}")
while True:
# Call the function to test it
     run_alexa()

