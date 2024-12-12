def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())

for j in range(N):
    M = int(input())

    if prime(M):
        print("YES")
    else:
        print("NO")
        
