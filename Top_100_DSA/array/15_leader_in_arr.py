def leader(arr):
    n = len(arr)
    ans = []
    max_ele = arr[-1]
    ans.append(max_ele)
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_ele:
            ans.append(arr[i])
            max_ele = arr[i]
    ans.reverse()
    return ans    

arr = [10,22,12,3,4,5,0,6]
print(leader(arr))


'''
def learder_in_arr(arr):
    
    ans = []
    n = len(arr)
    
    for i in range(n):
        leader = True
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                leader = False
                break
        if leader == True:
            ans.append(arr[i])
    return ans            
    
    
arr = [10,22,12,2,0,6]
print(learder_in_arr(arr))
'''