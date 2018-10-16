# Regex version of strip()
# Takes a string and does the same thing that strip() method does
# Takes whitespace chars like space, tab, and newline or a specific string and removes them from string beginning and end 
import re

def regexStrip(string, char2strip=''):

        if char2strip == '':
            notWhiteRegex = re.compile(r'^(\s*)(.*?)(\s*)$') # groups returns a tuple which can be indexed like tuple[1]
            if not notWhiteRegex.search(string) == None:
                strippedString = notWhiteRegex.search(string).group(2)
                print(strippedString)
        else:
            woCharRegex = re.compile(r'^(' + char2strip + '*)(.*?)(' + char2strip + '*)$') # had to get part from online
            if not woCharRegex.search(string) == None:
                strippedString = woCharRegex.search(string).group(2)
                print(strippedString)
 
regexStrip('   raghav   raghav   ')       
regexStrip('ABCraghavABCraghavABC', 'ABC')
