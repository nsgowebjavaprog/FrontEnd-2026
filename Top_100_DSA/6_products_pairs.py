def products_pairs(arr, target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] * arr[j] == target:
                return True
    return False

arr = [10, 20, 9, 40]
target = 4001

print(products_pairs(arr, target))