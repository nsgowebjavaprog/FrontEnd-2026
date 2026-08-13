def left_rotete_1_Place(arr):
    
    n = len(arr)
    
    if n <= 1:
        return arr
    
    first = arr[0]
    
    for i in range(n-1):
        arr[i] = arr[i+1]    # -------> O(n) , O(1)
    
    arr[n-1] = first
    return arr

arr = [1,2,3,4,5] # [2, 3, 4, 5, 1]
print(left_rotete_1_Place(arr))    