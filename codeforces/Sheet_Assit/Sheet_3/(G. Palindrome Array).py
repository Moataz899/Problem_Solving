N = int(input())

A = list(map(int, input().split()))

if A == A[::-1]:
    print("YES")

else :
    print("NO")
    
    