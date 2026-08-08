def miss_repeat(arr):
    n = len(arr)
    freq = [0] * (n+1)
    
    for num in arr:
        freq[num] = freq[num] + 1
    
    repeat = -1
    missing = -1
    
    for i in range(1, n+1):
        if freq[i] == 2:
            repeat = i
        elif freq[i] == 0:
            missing = i
    
    return missing, repeat

arr = [1,2,5,3,4,1]
print(miss_repeat(arr))