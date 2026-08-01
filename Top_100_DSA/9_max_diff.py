def max_difference(arr):

    if len(arr) < 2:
        return -1
    
    min_ele = arr[0]
    max_diff = -1
    
    for num in arr[1:]:
        if num > min_ele:
            max_diff = max(max_diff, num-min_ele)
        else:
            min_ele = num
    return max_diff            

# Example
arr = [4, 104, 3, 2, 1]

print(max_difference(arr))