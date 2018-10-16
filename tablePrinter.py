tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listOfLists):
    #displays lists of list with each list on a separate row
    #every row is right justified with equal spacing b/w each word
    colWidths = [0] * len(tableData)
    
    for i in range(len(tableData)): # 3
        for j in range(len(tableData[0])): # 4
            if colWidths[i] < len(tableData[i][j]):
                colWidths[i] = len(tableData[i][j])
           
    for i in range(len(tableData[0])): #index 0 to 3
        for j in range(len(tableData)): #indedx 0 to 2
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print('')
        
printTable(tableData)
