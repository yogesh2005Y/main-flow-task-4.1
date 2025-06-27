arr = list(map(int, input("Enter the numbers separated by space (one missing): ").split()))
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
print("Missing number is:",expected_sum - actual_sum)




