from gtts import gTTS
import os

file = open("numeric.txt","r")
myText = file.read().replace("\n"," ")
language = "hi"

output = gTTS(text = myText, lang = language, slow = False)
output.save("output.mp3")
file.close()
os.system("start output.mp3")