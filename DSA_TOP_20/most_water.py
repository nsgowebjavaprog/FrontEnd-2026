def most_water_storage(height):
    
    left = 0
    right = len(height)-1
    maxima = 0
    
    while left < right:
        width = right - left
        current = width * min(height[left], height[right])
        maxima = max(maxima, current)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxima            
    
    
height = list(map(int, input("Enter the height array elements: ").split()))

print(most_water_storage(height))    