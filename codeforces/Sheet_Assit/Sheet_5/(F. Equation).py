def Equation(N, X):
    quation = 0
    
    for i in range(0, N +1, 2):
        if i == 0:
            quation += X **i -1
        else :
            quation += X ** i
    
    return quation

x, n = map(int, input().split())

print(Equation(n, x))

