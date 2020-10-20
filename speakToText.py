import speech_recognition as sr 
 
r = sr.Recognizer() 

with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
try:
        print("Text: "+ r.recognize_google(audio, lang = 'en-EN'))
except:
        pass
