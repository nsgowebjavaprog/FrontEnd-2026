''' 
Problem Statement: You are climbing a staircase.

It takes n steps to reach the top.
Each time you can climb either: 1 step || 2 steps

Find the number of distinct ways to reach the top.
'''

# Dynamic Programming stores previous answers and avoids repeated work.

def clim_stairs(n):
    if n <= 2:
        return n
    
    first = 1
    second = 2
    
    for i in range(3, n+1):
        curr = first + second
        first = second
        second = curr
    return second

n = int(input("enter a number: "))
print(clim_stairs(n))