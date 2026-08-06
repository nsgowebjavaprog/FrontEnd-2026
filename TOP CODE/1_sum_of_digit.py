'''
n = 1234
o/p = 10
'''
'''
n = 1234
count = 0
while n > 0:
    rem = n % 10
    count = count + rem
    n = n //10
print(count)    
'''

'''
n = 1234
o/p = 10
'''

n = 1234
count = 0
while n > 0:
    count = count + n % 10
    n //= 10
print(count)    