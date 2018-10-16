#You may need to test the string against multiple regex patterns to validate its strength.
import re
print('Enter new password: ')
while True:

    password = input()
    eightCharRegex = re.compile(r'[a-zA-Z0-9]{8,}') # at least 8 char
    mo1 = eightCharRegex.search(password)
    upperCharRegex = re.compile(r'[a-z]+') # at least 1 lower case
    mo2 = upperCharRegex.search(password)
    lowerCharRegex = re.compile(r'[A-Z]+') #at least 1 upper case
    mo3 = lowerCharRegex.search(password)
    digitRegex = re.compile(r'[0-9]+') # at least 1 digit
    mo4 =digitRegex.search(password)

    
    if not (mo1 == None or mo2 == None or mo3 == None or mo4 == None):
        print(password + ' is your new password')
        break
    print('Password must have minimum 8 characters, uppercase and lowercase characters, and one digit.\nEnter stronger password: ')
