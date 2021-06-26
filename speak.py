from gtts import gTTS
import os

output = gTTS(text = "ok", lang = "en", slow=False)
output.save("speak.mp3")
os.system("speak.mp3")

