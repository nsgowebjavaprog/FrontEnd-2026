def check_arr_sorted_or_not(arr):
    '''
    sorted_arr = sorted(arr)
    return arr == sorted_arr
    '''
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True    
    
arr1 = [1,2,3,4,5,6,7,8,9]
# arr2 = [4,6,3,7,4,2,6,8,4,]
print(check_arr_sorted_or_not(arr1))