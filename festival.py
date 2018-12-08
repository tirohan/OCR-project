import os

import pytesseract
from PIL import Image




os.system('echo Welcome.  It is a pleasure to help you out|festival --tts ')
#os.system('fswebcam  -r 1280*720 --no-banner /home/pi/webcam "download.jpg" ')
im= Image.open("download.jpg")
text= pytesseract.image_to_string(im, lang = 'eng')
print(text)

file= open ("output.txt", "w")
file.write(text)
file.close()


os.system('festival --tts output.txt')
