T = int(input())

for i in range(T):
    T = int(input())
    factorial = 1
    
    for j in range(1, T + 1):
        factorial *= j
        
    print(factorial)
