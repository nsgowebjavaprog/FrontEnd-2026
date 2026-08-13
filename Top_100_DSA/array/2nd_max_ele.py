'''
arr = [10,20,30,40,50,60,70]

'''
def sec_large_ele(arr):
    if len(arr) < 2:
        return arr
    
    first_max = arr[0]
    sec_maxi = float("-inf")
    
    for curr_num in arr[1:]:
        if curr_num > first_max:
            sec_maxi = first_max
            first_max = curr_num
        
        else:
            if first_max > curr_num and sec_maxi < curr_num:
                sec_maxi = curr_num  
    return sec_maxi if sec_maxi != float("-inf") else -1             
    
arr = list(map(int, input("Enter arr elements: ").split()))
print("2nd Largest element: ", sec_large_ele(arr))