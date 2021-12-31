import math

def isEmpty(list):
    if len(list) < 1:
        return True
    else:
        return False

def evenElements(list):
    
    evenList = []
    
    if isEmpty(list):
        return evenList
    
    listLength = len(list)
        
    for i in range(listLength):
        if list[i] % 2 != 0:
            evenList.append(list[i])
    
    return evenList

list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print('List:', list)    
print('->Even Elements:', evenElements(list))
