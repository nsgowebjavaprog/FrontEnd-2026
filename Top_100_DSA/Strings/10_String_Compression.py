def String_Compression(s):
    res = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res.append(s[i-1] + str(count))
            count = 1
    
    res.append(s[-1] + str(count))
    return ''.join(res)                    

s = "aabcccccaaa"      # --------------> a2b1c5a3
print(String_Compression(s))