'''
If array have a number and if numbers have duplicates then return true
else return false
'''
''' Input: nums = [1,2,3,1]  --> Output: True '''
''' Input: nums = [1,2,3,4] --> Output: False '''

def duplicate_contains(nums):
    seen = set()
    for i in nums:
        if i in seen:   
            return True
        seen.add(i)
    return False

nums = list(map(int, input("Enter the array elements: ").split()))
print(duplicate_contains(nums))    