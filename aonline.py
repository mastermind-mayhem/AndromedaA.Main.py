import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
def encrypt(text):
    text = text.lower()
    full = ""
    alg = {
        "z": "a",
        "y": "b",
        "x": "c",
        "w": "d",
        "v": "e",
        "u": "f",
        "t": "g",
        "s": "h",
        "r": "i",
        "q": "j",
        "p": "k",
        "o": "l",
        "n": "m",
        "m": "n",
        "l": "o",
        "k": "p",
        "j": "q",
        "i": "r",
        "h": "s",
        "g": "t",
        "f": "u",
        "e": "v",
        "d": "w",
        "c": "x",
        "b": "y",
        "a": "z",
        " ": " ",
    }
    for decode in text:
        #print(alg[decode])
        full += alg[decode]
    print(full)

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")


def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        playsound.playsound("so.mp3")
        audio = r.listen(source)

        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


WAKE = "andromeda" and "Andromeda"
speak("Andromeda assistant services are coming online now")
speak("This assistant service was created by mastermind mayhem, and powered by python")

item1 = "nothing"

while True:

    text = get_audio()
#speech to text
    if "Andromeda Echo" in text:
        speak("I will write what you say starting now")
        echo = get_audio()
        print(echo)
#smalltalk
    if "hello" in text:
        speak("Hi! what is your name")
        name = get_audio()
        speak("Hello"+name+"How is your day going")
        text1 = get_audio()
        if "good" in text1:
            speak("that's good I hope that it stays that way")
        if "bad" in text1:
            speak("That is to bad, I hope it gets better")
#purpose
#purpose
    elif "what is your purpose Andromeda" in text:
        speak("I am a computer assistant meant to make your day easier")
#powerdown sequence
    elif "go to sleep" in text:
        speak("what is the deactivation passcode?")
        text = get_audio()
        if text == "Libya":
            speak("Powering Down Now")
            exit()
        else:
            speak("Im sorry that is incorrect")
#time
    elif "what is the time" in text:
        speak("the time is "+ time.strftime('%H %M'))
#calculator
    if "Andromeda calculator" in text:
        speak(", Which equation would you like (+ - * / ): ")
        equ = get_audio()
        if equ == "clear":
            exit()
        try:
            speak(input("What is your first number?: "))
            num1 = get_audio()
        except ValueError:
            speak("please enter a number")
            speak(input("What is your first number?: "))
            num1 = get_audio()
        try:
            speak(input("What is your second number?: "))
            num2 = get_audio()
        except ValueError:
            speak("please enter a number")
            speak(input("What is your second number?: "))
            num2 = get_audio()
        if "+" in equ:
            ans = (num1+num2)
            print(ans)

        if "-" in equ:
            ans = (num1-num2)
            print(ans)

        if "*" in equ:
            ans = (num1*num2)
            print(ans)

        if "/" in equ:
            ans = (num1/num2)
            print(ans)
#Options
    if "options" in text:
        speak("your options are")
        speak("hello andromeda")
        speak("what is your purpose")
        speak("what is the time")
        speak("Andromeda calculator")
        speak("my list")
#List
    if "my list" in text:
        speak("Which list would you like?")
        list = get_audio()
        if list == "1":
            speak("On your list currently is"+item1)
            speak("Would you like to change that?")
            itemans = get_audio()
            if itemans == "yes":
                speak("what would you like item 1 to be?")
                item1 = get_audio()
            if itemans == "no":
                speak("ok")
#encryption
    if "encrypt" in text:
        speak("what would you like to encrypt")
        en = input()
        try:
            encrypt(en)
        except KeyError:
            speak("please use only letters")
#jokes
    if "tell me a joke" in text:
        if joke == 5:
            speak("How did the dentist become a brain surgeon")
            time.sleep(2)
            speak("the drill slipped")
            joke = joke + 1
        if joke == 4:
            speak("Which clock is better analog or digital")
            time.sleep(3)
            speak("analog hands down")
            joke = joke + 1
        if joke == 3:
            speak("space holder")
            # time.sleep(2)
            # speak("the drill slipped")
            joke = joke + 1
        if joke == 2:
            speak("space holder")
            # time.sleep(2)
            # speak("the drill slipped")
            joke = joke + 1
        if joke == 1:
            speak("space holder")
            # time.sleep(2)
            # speak("the drill slipped")
            joke = joke + 1
        if joke >= 6:
            joke = 1

    if "stop listening" in text:
        speak("minutes or seconds")
        choi = get_audio()
        if "minutes" in choi:
            speak("How many minutes")
            timesl1 = int(get_audio())
            timesl1 = timesl1 * 60
            time.sleep(timesl1)
            speak("all done")
        if "seconds" in choi:
            speak("How many seconds")
            timesl2 = int(get_audio())
            time.sleep(timesl2)
            speak("all done")
