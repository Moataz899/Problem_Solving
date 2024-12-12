def count_non_decreasing_subarrays(arr):
    n = len(arr)
    count = 0
    length = 1

    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            length += 1
        else:
            count += (length * (length + 1)) // 2
            length = 1

    count += (length * (length + 1)) // 2
    return count

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    result = count_non_decreasing_subarrays(numbers)
    results.append(result)

for result in results:
    print(result)
