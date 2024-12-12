import math

A, B, X = map(int, input().split())
low = min(A, B)
high = max(A, B)

first_divisible = (low + X - 1) // X * X
last_divisible = high // X * X

if first_divisible > high:
    print(0)
else:
    n = (last_divisible - first_divisible) // X + 1
    total_sum = (n * (first_divisible + last_divisible)) // 2
    print(total_sum)
