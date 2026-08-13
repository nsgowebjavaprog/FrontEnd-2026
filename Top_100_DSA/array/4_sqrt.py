class Solution:
    def mySqrt(self, x):

        # Handle small cases
        if x < 2:
            return x

        left = 1
        right = x
        ans = 0

        while left <= right:

            # Safe middle calculation
            mid = left + (right - left) // 2

            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                ans = mid          # Current possible answer
                left = mid + 1     # Try finding a larger sqrt

            else:
                right = mid - 1    # Search smaller values

        return ans


# User Input
x = int(input("Enter number: "))

obj = Solution()
print(obj.mySqrt(x))