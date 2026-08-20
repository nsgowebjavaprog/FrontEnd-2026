def gcd_or_hcf(a,b):
    
    a = abs(a)
    b = abs(b)
    
    while b:
        a,b = b, a%b
    return a

a = 48
b = 18

print(gcd_or_hcf(a,b))    