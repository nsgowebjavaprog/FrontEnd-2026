def first_non_reapiting_char(s):
    count = [0] * 256
    
    for ch in s:
        count[ord(ch)] += 1
    
    for ch in s:
        if count[ord(ch)] == 1:
            return ch
    
    return None

s = 'swiwss'
print(first_non_reapiting_char(s))        