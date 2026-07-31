class Solution:
    def searchRange(self, nums, target):

        # Find the first occurrence of target
        def findFirst():
            left = 0
            right = len(nums) - 1
            ans = -1      # Store first occurrence

            while left <= right:

                # Safe way to calculate middle
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid              # Store current answer
                    right = mid - 1        # Continue searching on LEFT

                elif nums[mid] < target:
                    left = mid + 1         # Search right half

                else:
                    right = mid - 1        # Search left half

            return ans


        # Find the last occurrence of target
        def findLast():
            left = 0
            right = len(nums) - 1
            ans = -1      # Store last occurrence

            while left <= right:

                # Safe middle calculation
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid              # Store current answer
                    left = mid + 1         # Continue searching on RIGHT

                elif nums[mid] < target:
                    left = mid + 1         # Search right half

                else:
                    right = mid - 1        # Search left half

            return ans

        # Return [first occurrence, last occurrence]
        return [findFirst(), findLast()]


# User Input
nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

obj = Solution()
print(obj.searchRange(nums, target))