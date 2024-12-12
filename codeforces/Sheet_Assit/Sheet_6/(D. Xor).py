A, B , Q = map(int, input().split())
Xor = A ^ B

if (Q - 1) % 3 == 0:
    element = A

elif (Q - 1) % 3 == 1:
    element = B

else:
    element = Xor
    
print(element)