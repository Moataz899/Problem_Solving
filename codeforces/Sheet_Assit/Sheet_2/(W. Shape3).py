N = int(input())

for i in range(1 , N + 1):
    print(' ' * (N - i), end='')
    print('*' * (2 * i - 1))
    
for j in range(N , 0, -1):
    print(' ' * (N - j), end='')
    print('*' * (2 * j -1))
    