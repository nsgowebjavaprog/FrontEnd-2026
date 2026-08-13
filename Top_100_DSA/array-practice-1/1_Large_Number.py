def large_ele(arr):
    '''
    arr.sort()
    return arr[-1]
    '''
    # O(n log(n))

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest         
    # O(n)
    
arr = [1,4,7,2,9,32,5]
print(large_ele(arr))