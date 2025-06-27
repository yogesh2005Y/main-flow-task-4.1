def find_subarray_with_sum(arr, target):
    start = 0
    current_sum = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return (start, end)
    return -1


print(find_subarray_with_sum([1, 2, 3, 7, 5], 12)) 
