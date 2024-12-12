N = int(input())

if N == 1 :
    print(0)

elif N == 2:
    print(1)

else :
    a, b = 0, 1
    
    for i in range(3, N + 1):
        a, b = b, a + b
        
    print(b)
