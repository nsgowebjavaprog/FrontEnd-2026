'''
Input:
s = "anagram"
t = "nagaram"   Output: True
'''
# Every character appears the same number of times.

def anagram_checker(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count = {} # Empty Dictionary
    
    for ch in str1:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in str2:
        if ch not in count:
            return False
        
        # If Present
        count[ch] -= 1
        
        # Optional
        if count[ch] < 0: # or if count[ch] == 0: 
            return False
    return True    
        
    
str1 = input("Enter the first string: ")    
str2 = input("Enter the second string: ")

print(anagram_checker(str1, str2))