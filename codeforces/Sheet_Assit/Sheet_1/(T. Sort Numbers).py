A, B, C = map(int, input().split())

numbers = [A, B, C]

if A > B :
    A, B = B, A

if B > C :
    B, C = C, B

if A > B :
    A, B = B, A
    
print(A)
print(B)
print(C)
 
print()
 
print(numbers[0])
print(numbers[1])
print(numbers[2])