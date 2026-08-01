def twoSum(arr, target):
    seen = {} # Dict
    
    for i, num in enumerate(arr):
        needed = target - num
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i
        
    return -1

arr = [2,7,11,15]
target = 19

print(twoSum(arr, target))    