##


def bubleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
    return list

#print(bublesort([2,1,5,3,4]))

def gnomeSort(list):
    i = 0
    while i < len(list)-1:
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            
            if i > 0: i-=1
        else: i+=1
        
    return list

#print(gnomeSort([2,1,5,3,4]))

def selectionSort(list):
    for i in range(len(list)-1):
        min = list[i]
        minPos = i
        j = i
        while j < len(list):
            if list[j] < min: 
                min = list[j]
                minPos = j
            j+=1
        temp = list[i]
        list[i] = min
        list[minPos] = temp
    
    return list

#print(selectionSort([2,1,5,3,4,9,6,8,10,7]))

def shakerSort(list):
    for i in range(len(list)-1):
        j = 0 
        while j < len(list)-1-i:
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
            j+=1
            
        while j > i:
            if list[j] < list[j-1]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
                
            j-=1
            
    return list

print(shakerSort([2,1,5,3,4,9,6,8,10,7]))