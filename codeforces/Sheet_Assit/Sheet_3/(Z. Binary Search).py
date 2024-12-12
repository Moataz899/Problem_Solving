def binary_search(arr, n):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == n:
            return True
        elif arr[mid] < n:
            left = mid + 1  
        else:
            right = mid - 1
    return False

N, Q = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    num = int(input())
    
    if binary_search(A, num):
        print("found")
    else:
        print("not found")
