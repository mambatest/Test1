from gtts import gTTS
import os
mytext = 'Bonjour tout le monde. Voici mon premier program'


language = 'fr'


myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("start welcome.mp3")