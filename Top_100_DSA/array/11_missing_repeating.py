def repeating_and_missing(arr):
# arr = [4, 3, 6, 2, 1, 1]  o/p ==> [1,5]
    n = len(arr)
    
    # SuM 
    expected_sum = n * (n+1) // 2  # 42/2 --> 21    
    diif_sum = expected_sum - sum(arr)   # 21-17 = 4
   
    # Square-SuM 
    expected_sq_sum = n * (n+1) * (2*n+1) // 6   # 91
    diff_sq_sum = expected_sq_sum - sum(i*i for i in arr)  # 91 - 67 == 24
    
    sum_missing_and_repe = diff_sq_sum // diif_sum  # 24/4 = 6
    
    missing = (diif_sum + sum_missing_and_repe) // 2  # 4+6/2 == 5
    repeating = missing - diif_sum   # 5-1 == 1
    
    return [repeating, missing]

arr = [4, 3, 6, 2, 1, 1]
print(repeating_and_missing(arr))