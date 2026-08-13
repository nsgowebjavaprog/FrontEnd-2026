def small_ele(arr):
    '''
    arr.sort()
    return arr[0]
    '''
    # O(n log(n))
    
    small = arr[0]
    for num in arr:
        if num < small:
            small = num   # O(n)
    return small        
    
arr = [3,6,9,2,4,8,1,5,7]
print(small_ele(arr))