def left_rotate_1_place(arr):
    n = len(arr)
    if n<2:
        return arr
    
    first = arr[0]
    
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = first
    return arr

arr = [1,2,3,4,5,6]
print(left_rotate_1_place(arr))