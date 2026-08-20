def is_perfect(n):
    
    if n<=1:
        return False
    
    original = n
        
    total = 1
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            total += i
            
            if i != n//i:
                total += n//i
                
    return total == original
    
n = 6 # 6 --> 1,2,3 [1+2+3 = 6] Ok it's a Perfect Number
print(is_perfect(n))