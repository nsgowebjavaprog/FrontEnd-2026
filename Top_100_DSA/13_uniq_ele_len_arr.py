def uniq_ele_len_arr(arr):
    
    if len(arr) == 0:
        return 0
    
    i=0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1

arr = [0,1,1,1,2,2,3,3,3,3,3,3,3,4,4,4]
print(uniq_ele_len_arr(arr))        