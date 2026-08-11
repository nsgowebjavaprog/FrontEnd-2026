def Anagram(s,t):
    if len(s) != len(t):
        return False
    
    count = {}
    
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in t:
        count[ch] = count.get(ch, 0) - 1
    
    for num in count.values():
        if num != 0:
            return False
    return True

print(Anagram('listen', 'silant'))                