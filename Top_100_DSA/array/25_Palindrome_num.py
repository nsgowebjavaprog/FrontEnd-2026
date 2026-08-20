def Palindrome_num(n):
    if n < 0:
        return False
    
    original = n
    rev = 0
    
    while n > 0:
        last_dig = n % 10
        rev = rev * 10 + last_dig
        n //= 10
    return original == rev

n = 123216
print(Palindrome_num(n))    