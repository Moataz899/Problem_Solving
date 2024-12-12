def diff(A):
    return min(A), max(A)

N = int(input())
A = list(map(int, input().split()))

ouput = diff(A)

print(*ouput)
