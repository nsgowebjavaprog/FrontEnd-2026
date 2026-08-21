# def first_occurence(arr, k):
#     for i in range(len(arr)):
#         if arr[i] == k:
#             return i
#     return -1

def last_occurence(arr, k):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == k:
            return i
    return -1

arr = list(map(int, input().split())) 
k = int(input()) 
print(last_occurence(arr, k)) 