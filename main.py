import tkinter as tk
from googletrans import Translator
from gtts import gTTS
import os

root= tk.Tk()
root.title("Translate")

can = tk.Canvas(root, width = 500, height = 250)
can.pack()

entry = tk.Entry(root) 
can.create_window(250, 50, window=entry, width = 500, height = 30)

def getText():
        return entry.get()


def translate(textInput):
        result = Translator().translate(textInput, "vi").text
        lang = "vi"
        if(result == textInput):
                result = Translator().translate(textInput, "en").text
                lang = "en"
        return result, lang

def show():
    result, lang = translate(getText())
    
    global textOutput
    global langOutput
    
    textOutput = result
    langOutput = lang
    
    label = tk.Label( root,text=textOutput)
    can.create_window(250, 150, window=label, width = 500, height = 40)
      

def speak(txt, language):
    output = gTTS(text = txt , lang = language , slow=False)
    output.save("speak.mp3")
    os.system("speak.mp3")

def changeLanguage(lang):
        if(lang == "vi"):
                return "en"
        if(lang == "en"):
                return "vi"

def onClick(tick):
        try:
            if(tick==0):
                lang = changeLanguage(langOutput)
                speak(getText(), lang)
            if(tick==1):
                speak(textOutput, langOutput)
        except:
                print("you need click change!")
    
btnChange = tk.Button(text='Change', command=show)
can.create_window(250, 100, window=btnChange)

btnSpeakDefault = tk.Button(text='SpeakDefault', command=lambda: onClick(0))
can.create_window(100, 100, window=btnSpeakDefault)

btnSpeak = tk.Button(text='Speak', command=lambda: onClick(1))
can.create_window(250, 200, window=btnSpeak)

root.mainloop()
