arr = list(map(int,input("Enter a sorted list of numbers:").split()))
target = int(input("Enter the target number:"))
low, high = 0, len(arr) - 1
index = -1

while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            index = mid
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
print("Target found at index:" if index !=-1 else "Target not found:", index)