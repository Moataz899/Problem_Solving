import math
 
A, B = map(int, input().split())
 
f = math.floor(A / B)
c = math.ceil(A / B)
 
if A % B >= B / 2:
    r = math.ceil(A / B)
else:
    r = math.floor(A / B)
 
print("floor", A, "/", B, "=", f)
print("ceil", A, "/", B, "=", c)
print("round", A, "/", B, "=", r)
