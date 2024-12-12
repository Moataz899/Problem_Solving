def Swap(X, Y):
    X, Y = Y, X
    return X, Y
    
x, y = map(int, input().split())

X, Y = Swap(x, y)

print(X, Y)

