import os
from datetime import datetime

path = input("enter file path: ")

if os.path.exists(path): 
    print("file exists")
else: 
    print("Incorrect File Path")
    exit()

if os.path.isdir(path):
    print("this is a folder")
    print("files inside this folder:")
    files = os.listdir(path)
    print(files)

elif os.path.isfile(path):
    print("this is a file")

    size = os.path.getsize(path)
    print("size:", size, "bytes")

    stats = os.stat(path)
    print("Created:", datetime.fromtimestamp(stats.st_ctime))
    print("Modified:", datetime.fromtimestamp(stats.st_mtime))

ext = os.path.splitext(path)[1]
print("Extension:", ext)
if ext in [".png", ".jpg", ".jpeg"]:
    print("Image")
elif ext in [".txt"]:
    print("Text")
elif ext in [".mp4", ".mov"]:
    print("Video")
else:
    print("unknown or unsupported")

