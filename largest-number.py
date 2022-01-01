def largestNumber(list):
    
    #number = max(list)
    
    listLength = len(list)
    
    number = 0
    
    for i in range(listLength):
        
        if  list[i] > number:
            number = list[i]
    
    return number

list = [23,54,1,3,9,67,77,44]
list1 = [77,54,1,3,9,67,23,44]
list2 = [44,54,1,3,9,67,23,77]
list3 = [7]
list4 = []

print('List:', list)    
print('->Largest Number:', largestNumber(list))
print('->Largest Number1:', largestNumber(list1))
print('->Largest Number2:', largestNumber(list2))
print('->Largest Number3:', largestNumber(list3))
print('->Largest Number4:', largestNumber(list4))