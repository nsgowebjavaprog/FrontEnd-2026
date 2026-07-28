''' 
Input:
s = "A man, a plan, a canal: Panama"

Output:
True
'''

def palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Optional
        while left < right and not s[left].isalnum():
            left += 1
        # Optional
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True

s = input("Enter I/P: ")        
print(palindrome(s))