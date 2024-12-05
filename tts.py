from gtts import gTTS

import pygame

mytext = input()

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("welcome.mp3")

pygame.mixer.init()

pygame.mixer.music.load("welcome.mp3")

pygame.mixer.music.play()