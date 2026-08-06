def repeat_miss(arr):
    n = len(arr)
    freq = [0] * (n+1)

    for num in arr:
        freq[num] += 1
    
    repeat = miss = -1    

    for i in range(1, n+1):
        if freq[i] == 2:
            repeat = i
        elif freq[i] == 0:
            miss = i 
    return miss, repeat 

arr = [1,6,4,5,3,1]
print(repeat_miss(arr))           

'''
def missing_reapiting(arr):
    n= len(arr)
    missing = repeating = -1
    
    for i in range(1, n+1):
        count = 0
        
        for num in arr:
            if num == i:
                count+=1
        if count ==2:
            repeating = i
        elif count==0:
            missing = i 
    return missing, repeating                    

arr = [1,3,4,5,6,1]
print(missing_reapiting(arr))
'''