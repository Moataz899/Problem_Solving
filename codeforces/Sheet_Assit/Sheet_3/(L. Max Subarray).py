def max_subarray(arr):
    max_nums = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            max_nums.append(max(arr[i:j+1]))
    return max_nums

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    max_numbers = max_subarray(numbers)
    results.append(max_numbers)

for result in results:
    print(*result)
