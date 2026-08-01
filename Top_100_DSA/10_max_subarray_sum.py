def max_subArray_Sum(arr):
    
    curr_sum = arr[0]
    max_sum = arr[0]
    
    for num in arr[1:]:
        curr_sum = max(num, curr_sum+num)
        max_sum = max(max_sum, curr_sum)
    return max_sum    
    
arr = [2, 3, -8, 7, -1, 2, 3]
print("Max SubArray Sum: ", max_subArray_Sum(arr))