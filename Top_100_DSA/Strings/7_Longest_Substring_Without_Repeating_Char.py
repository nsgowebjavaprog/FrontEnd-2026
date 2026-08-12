def Longest_Substring_Without_Repeating_Characters(s):
    dict = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in dict and dict[s[right]] >= left:
            left = dict[s[right]]+1
        
        dict[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

s = 'abcabccb'
print(Longest_Substring_Without_Repeating_Characters(s))        