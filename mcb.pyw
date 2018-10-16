#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip2, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip2.paste()
   
   
elif len(sys.argv) == 2:  
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip2.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1] in mcbShelf:
        pyperclip2.copy(mcbShelf[sys.argv[1]])

    elif sys.argv[1].lower() == 'delete':
        for i in mcbShelf.keys():
            del mcbShelf[i]
        
mcbShelf.close()

