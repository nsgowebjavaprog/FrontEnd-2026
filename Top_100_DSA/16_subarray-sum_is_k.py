def sub_array_sum_equals_k(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total = total + arr[j]
            
            if k == total:
                count += 1
    return count            
arr = [1,2,3]
k = 3
print(sub_array_sum_equals_k(arr,k))