def shift_zeros(arr):
   return [num for num in arr if num != 0] + [0] * arr.count(0)
        
N = int(input())
A = list(map(int, input().split()))

print(*shift_zeros(A))