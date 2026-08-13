def find_duplicates(arr):
    '''
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return -1
    '''
    # O(n log(n))
    
    seen = set()
    for num in arr:
        if num in seen:     # ----> O(n)----&----O(n)
            return num
        
        seen.add(num)
    return -1    

arr = [1,2,3,4,5,6]
print(find_duplicates(arr))            