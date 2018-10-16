#! python3
# regexfilesearch.py - takes user-supplied regex and prints all matches
# found in all text files within a folder

import os, re

print("Enter regular expression using appropriate conventions: ")
regexObject = re.compile(input())
print("Enter folder file path containing text files (no escape charsss): ")
folderPath = input()
# user should enter as folder path -> C:\Users\ragha\Documents\New folder

if os.path.exists(folderPath) == True:

    for filename in os.listdir(folderPath):
        fileObj = open(os.path.join(folderPath, filename), 'r')
        fileString = fileObj.read()
        mo = regexObject.findall(fileString)

        for i in range(len(mo)):
            print(mo[i])
