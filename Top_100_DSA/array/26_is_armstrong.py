def is_armstrong(n):
    if n < 0:
        return False
    
    original_val = n
    no_of_dig = len(str(n))
    total = 0
    
    while n>0:
        last_dig = n % 10
        total = total + (last_dig ** no_of_dig)
        n //= 10
    return total == original_val

n = 153
print(is_armstrong(n))