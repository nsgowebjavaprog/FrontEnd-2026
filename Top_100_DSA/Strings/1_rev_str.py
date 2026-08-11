def rev_str(s):
    chars = list(s)
    left = 0
    right = len(chars)-1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars) 
    
    
s = "HellO"
print(rev_str(s))