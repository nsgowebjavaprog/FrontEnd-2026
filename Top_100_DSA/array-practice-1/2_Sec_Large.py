def sec_large(arr):
    '''
    arr.sort()
    n = len(arr)
    for i in range(n-2, -1, -1): 
        if arr[i] != arr[-1]:
            return arr[i]
    return -1
    '''
    # O(n log(n))
    
    
    largest = sec = float('-inf')
    for num in arr:
        if num > largest:
            sec = largest
            largest = num
        
        elif num > sec and num != largest:   # ---->  O(n)
            sec = num
    return sec if sec != float('-inf') else -1            

arr = [236,236,236,236]
print(sec_large(arr))