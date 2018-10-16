#! python 3
# fillinthegaps.py - go through folder containing files titled "spam001.txt",
# "spam002.txt, spam003.txt and if there are any gaps, have the pgm rename
#all the later files to fill in the gaps

import os, re, shutil
  
def fillingaps(foldername):
    breakpoint = 0
    while breakpoint !=-1:    
        regexObject = re.compile(r'^(spam)(0*)(\d+)(.txt)')
        lst = []
        breakpoint=-1
        
        for folder, subfolders, filenames in os.walk(foldername):
            for filename in filenames:
                mo = regexObject.search(filename)
                if mo != None: 
                    lst.append(int(mo.group(3)))

        lst.sort()   
        for i in range(len(lst)):
            if (i+1) == lst[i]:
                print(lst[i])
            else:
                  print(str(lst[i]-1) + ' is missing.')
                  breakpoint = lst[i]-1
                  break
                
        if breakpoint!= -1:
            for folder, subfolders, filenames in os.walk(foldername):
                for filename in filenames:
                    mo = regexObject.search(filename)
                    if int(mo.group(3))>breakpoint:
                        newfilename = mo.group(1) + mo.group(2) + str(int(mo.group(3))-1) + mo.group(4)
                        if mo.group(3)=='10' or mo.group(3)=='100':
                            newfilename = mo.group(1) + mo.group(2) + '0' + str(int(mo.group(3))-1) + mo.group(4)

                        print('%s changed to %s' % (os.path.join(foldername,filename), os.path.join(foldername, newfilename)))
                        shutil.copy(os.path.join(foldername,filename), os.path.join(foldername, newfilename))
                        os.unlink(os.path.join(foldername,filename)) 

fillingaps(r'C:\Users\ragha\Documents\New folder')



