def Longest_Common_Prefix(s):
    if not s:
        return " "
    
    prefix = s[0]
    
    for i in range(1, len(s)):
        while not s[i].startswith(prefix):
            prefix = prefix[:-1]
            
            if not prefix:
                return " "
    return prefix
s = ["flower", "flow", "flight"]
print(Longest_Common_Prefix(s))