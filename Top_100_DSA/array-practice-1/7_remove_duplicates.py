def remove_duplicates(arr):
    if not arr:
        return 0
    
    i=0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i=i+1
            arr[i] = arr[j]
    return i+1 

arr = [0,1,2,2,2,3,4,4,4]  # 5
print(remove_duplicates(arr))       