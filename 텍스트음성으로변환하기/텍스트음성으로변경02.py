from gtts import gTTS
from playsound import playsound
import os

os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(os.getcwd())))

text = "뽀리바보 나는 해결했다."

tts = gTTS(text=text, lang="ko")
tts.save("test.mp3")

playsound("test.mp3")
