import os

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
    print("Created:", stats.st_ctime)
    print("Modified:", stats.st_mtime)
