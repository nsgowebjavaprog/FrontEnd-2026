''' Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum, 
and return that sum. '''

'''
current_sum = max(num, current_sum + num)

maximum_sum = max(maximum_sum, current_sum)
'''

# O(n) || O(1)

def max_sub_array(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

nums = list(map(int, input("Enter array elements: ").split()))
print("Maximum subarray sum: ", max_sub_array(nums))        