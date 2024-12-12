N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0 , 0

while i < len(A) and j < len(B):
    if A[i] == B[j]:
       j += 1
    i += 1

if j == M:
    print("YES")

else:
    print("NO")