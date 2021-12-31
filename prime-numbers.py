import math

def isEmpty(list):
    if len(list) < 1:
        return True
    else:
        return False

def isPrime(n):
    
    aux = (int)(math.sqrt(n))
    
    for x in range(2, aux+1):
        if n % x == 0:
            return False 
    return True

def primeElements(list):
    
    # Divisible for 1 and for himself
    
    if isEmpty(list):
        return list
    
    listLength = len(list)
    primeList = []
    
    for i in range(listLength):
        if isPrime(list[i]):
            primeList.append(list[i])
    
    return primeList
    
list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print('List:', list)    
print('->Prime List:', primeElements(list))
