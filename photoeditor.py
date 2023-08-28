import time
from PIL import Image, ImageEnhance, ImageFilter
import os

print("Welcome to my first Photo-Editor. " +
      "Its not much, but hey...its fully automatic! ")
print("Put your Pics in the IMG Folder")
print("Wait 2 Seconds before Continuing!")
time.sleep(2)

path = './img'
pathOut = '/edited'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("L")

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')

print("Now your files are ready in the -edited- folder! ")
print("Thanks for using my automatic photo editor")
