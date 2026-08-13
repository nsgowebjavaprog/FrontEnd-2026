'''
def left_rotete_by_D_places(arr,d):

    n = len(arr)
    if n==0:
        return arr
    
    d = d % n
    temp = arr[:d]
    
    for i in range(d,n):
        arr[i-d] = arr[i]
        
    for i in range(d):
        arr[n-d+i] = temp[i]
        
    return arr
    '''

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def d_places(arr, d):
    n= len(arr)
    
    if n == 0:
        return n
    
    d = d % n
            
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0,n-1)

    return arr
    
arr = [1,2,3,4,5]
d = 2
print(d_places(arr, d))        