#! python 3

import os
for i in range(1,10):
    fileObject = open(r'C:\Users\ragha\Documents\New folder\spam00' + str(i) +'.txt', 'w')
    fileObject.close()
for i in range(10,100):
    fileObject = open(r'C:\Users\ragha\Documents\New folder\spam0' + str(i) +'.txt', 'w')
    fileObject.close()
for i in range(100,1001):
    fileObject = open(r'C:\Users\ragha\Documents\New folder\spam' + str(i) +'.txt', 'w')
    fileObject.close()


    
