'''
def two_sum(nums, target):

    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

nums = [2,5,8,9]
target = 7

print(two_sum(nums, target))
'''
# Optimal

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        need = target - num
        
        if need in hashmap:
            return [hashmap[need], i] # curr, need
        # Store in hashmap
        hashmap[num] = i
    return []

nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

res = twoSum(nums, target)

print("Indices: ", res)