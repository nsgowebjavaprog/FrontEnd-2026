def factor(n):
    for i in range(1, int(n ** 0.5)+1 ):
        if n%i == 0:
            print(i, end=",")
            
            if i != n//i:
                print(n//i, end=",")
print(factor(36))                

# 1,2,3,4,6

# 1 != 36 --- ok
# 2 != 36 --- ok
# 3 != 36 --- ok
# 4 != 36 --- ok
# 6 != 36//6 --------- NO

# 1,36,2,18,3,12,4,9,6