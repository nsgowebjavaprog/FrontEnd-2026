def merge_2_sorted_arr(arr1, arr2):
    
    i = len(arr1)-1
    j = 0
    
    while i>=0 and j<len(arr2):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            
            i = i-1
            j = j+1
        else:
            break
    arr1.sort()
    arr2.sort()     
    
    return arr1, arr2       


arr1 = [0,1,4,5]
arr2 = [2,3,6,7,8]
print(merge_2_sorted_arr(arr1, arr2))