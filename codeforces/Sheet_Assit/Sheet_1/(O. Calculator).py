X = input().strip()

if '+' in X :
    a, b = map(int, X.split('+'))
    print(a + b)

elif '-' in X :
    a, b = map(int, X.split('-'))
    print(a - b)
    
elif '*' in X :
    a, b = map(int, X.split('*'))
    print(a * b)
    
elif '/' in X :
    a, b = map(float, X.split('/'))
    print(int(a / b))
