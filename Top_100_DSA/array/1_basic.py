arr_size = int(input("Enter the size of array: "))
arr_ele = list(map(int, input("Enter elements: ").split()))

print("----Array Elements----")

for i in range(arr_size):
    print(arr_ele[i], end=" ")