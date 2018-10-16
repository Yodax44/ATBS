#! python3
# print100mbfiles.py - walks though folder tree and searches for
# big files (100mb+) and prints their name and size

import os

def printbigfiles(folder):
    for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
        for filename in filenames:
            if (int(os.path.getsize(os.path.join(foldername, filename))) > 100*10*10*10*10*10*10):
                print('filename: %s and file size: %s\n' %(filename, os.path.getsize(os.path.join(foldername, filename))))

printbigfiles(r'C:\Users\ragha\Downloads')

