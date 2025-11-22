import os
from datetime import datetime

path = input("Enter file path: ")

if os.path.exists(path): 
    print("File Exists")
else: 
    print("Incorrect File Path")
    exit()

if os.path.isdir(path):
    print("This is a folder.")
    print("Files inside this folder:")
    files = os.listdir(path)
    print(files)

elif os.path.isfile(path):
    print("This is a file.")

    size = os.path.getsize(path)
    print("Size:", size, "bytes")

    stats = os.stat(path)
    print("Created:", datetime.fromtimestamp(stats.st_ctime))
    print("Modified:", datetime.fromtimestamp(stats.st_mtime))

ext = os.path.splitext(path)[1]
print("Extension:", ext)
if ext in [".png", ".jpg", ".jpeg"]:
    print("Type: Image")
elif ext in [".txt"]:
    print("Type: Text file")
elif ext in [".mp4", ".mov"]:
    print("Type: Video")
else:
    print("Type: Unknown or unsupported")

