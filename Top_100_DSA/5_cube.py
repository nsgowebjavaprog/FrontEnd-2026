def cube_root(n):
    if n<2:
        return n
    
    left = 0
    right = n
    ans = 0
        
    while left <= right:
        mid = left + (right -left) // 2
        cube = mid*mid*mid
        
        if cube == n:
            return mid
        
        elif cube < n:
            ans=mid
            left = mid+1
        
        else:
            right = mid-1
    return ans            
n = int(input("Enter number: "))
print("Cube is; ", cube_root(n))