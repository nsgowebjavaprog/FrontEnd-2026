def arr_sort_or_not(arr):
    n = len(arr)
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True


# arr = [1,2,3,4,7,6,7,8,9]  -- > False
arr = [1,2,3,4,5,6,7,8,9]    # --> True
print(arr_sort_or_not(arr))