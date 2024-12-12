N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = A.sort()
B_sorted = B.sort()

if A == B :
    print('yes')

else :
    print('no')
    