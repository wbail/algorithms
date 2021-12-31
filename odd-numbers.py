import math

def isEmpty(list):
    if len(list) < 1:
        return True
    else:
        return False

def oddElements(list):
    
    oddList = []
    
    if isEmpty(list):
        return oddList
    
    listLength = len(list)
    
    for i in range(listLength):
        if list[i]%2 == 0:
            oddList.append(list[i])
    
    return oddList

list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print('List:', list)    
print('->Odd Elements:', oddElements(list))
