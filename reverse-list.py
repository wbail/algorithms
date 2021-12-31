def reverseList(list):
    
    listLength = len(list)
    
    for i in range(listLength//2):
        aux = list[i]
        #print('Aux:', aux)
        list[i] = list[(listLength-1)-i]
        #print('List[i]: ', list[i])
        list[(listLength-1)-i] = aux
        #print('List[listLength-1]: ', list[listLength-1])
        #print('new list: ', list)
    
    return list

list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print('List:', list)    
print('->Reversed List:', reverseList(list))
