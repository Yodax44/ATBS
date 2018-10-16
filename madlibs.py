#! python3
# mad libs game

import os, re

fileObj = open(r'C:\Users\ragha\MyPythonScripts\madlibs.txt')
listofStrings=fileObj.read()
fileRegex = re.compile(r'NOUN|ADJECTIVE|VERB')
mo= fileRegex.findall(listofStrings)

#convert the string found in file into a list separated at each instance of noun, adjective, or verb
temp = 'x'.join(listofStrings.split('NOUN'))
temp = 'x'.join(temp.split('ADJECTIVE'))
temp = 'x'.join(temp.split('VERB'))
temp = temp.split('x')

j=1
# ask user for input based on mo object and insert input in list generated above.
for i in range(len(mo)):
    if mo[i]== 'ADJECTIVE':
        print('Enter an adjective: ')
    else:
        print('Enter a ' + mo[i].lower() + ': ')
    temp.insert(j, input())
    j=j+2

print(''.join(temp))

