import math

A, B, C, D = map(int, input().split())

if (1 <= A <= 10**7 and 1 <= C <= 10**7) and (1 <= B <= 10**12 and 1 <= D <= 10**12):
    if B * math.log(A) > D * math.log(C):
        print('YES')
    else:
        print('NO')

