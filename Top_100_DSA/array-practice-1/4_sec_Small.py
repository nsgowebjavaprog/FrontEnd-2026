def sec_small_ele(arr):
    '''   
    small = secSmall = float('inf')
    arr.sort()
    
    for i in range(1, len(arr)+1):
        if arr[i] != arr[0]:
            return arr[i]
    return -1        
    '''
    # O(n log(n))
    
    small = secSmall = float('inf')
    
    for num in arr:
        if num < small:
            secSmall = small
            small = num
            
        elif num <secSmall and num != small: # ----->  O(n)
            secSmall = num
    return secSmall

arr = [3,6,9,2,4,8,11,5,7]
print(sec_small_ele(arr))