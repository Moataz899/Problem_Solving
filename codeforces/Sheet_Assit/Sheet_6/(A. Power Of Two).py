import math

N = int(input())

if math.log2(N).is_integer():
    print("YES")
else:
    print("NO")
    