# comma code project
# this project takes a list and converts to a string with
# commas between each item and an "and" inserted before the last item

def commaCode(list1):
 
    string1 = ''
    for i in range(len(list1)-1):
        string1 += list1[i] + ', ' 
    string1 += 'and ' + list1[-1]

    return string1
    
