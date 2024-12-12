def Wonderful(n):
    if n %2 != 0 and bin(n)[2:] == bin(n)[2:][::-1]:
        print('YES')
    else :
        print('NO')
        
N = int(input())

Wonderful(N)

