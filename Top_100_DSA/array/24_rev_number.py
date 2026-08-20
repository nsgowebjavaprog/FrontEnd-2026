def rev_number(n):
    
    sign = -1 if n<0 else 1
    
    n = abs(n)
    
    rev_number = 0
    while n>0:
        last_dig = n % 10
        rev_number = rev_number * 10 + last_dig
        n //= 10
    return sign * rev_number

n = -12345
print(rev_number(n))    