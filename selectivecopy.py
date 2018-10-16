#! python3
#selectivecopy.py - this python program walks through a folder tree
#and searches through files certain file extension (.pdf or .jpg) and
#copies these files from whatever location they are in to a new folder

import os, shutil

def selcopy(sourcefolder, destfolder):

    for foldername, subfolders, filenames in os.walk(sourcefolder):
        print('Copying all jpg and pdf files from %s to %s' % (foldername, destfolder))

        for filename in filenames:
            if filename.endswith('.jpg') or filename.endswith('.pdf'):
                shutil.copy(os.path.join(foldername,filename), destfolder)

selcopy(r'C:\Users\ragha\Documents', r'C:\Users\ragha\Desktop\New folder')
