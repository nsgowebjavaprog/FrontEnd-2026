def rev_words(s):
    
    words = s.split()
    res = []
    
    for word in words:
        res.append(word[::-1])
    return ' '.join(res)   # I EVOL uOY
    
    # return res # ['I', 'EVOL', 'uOY']
    
s = "I LOVE YOu"
print(rev_words(s))    