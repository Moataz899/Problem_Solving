import math

def prime(n):
    if n <= 1:
        print("NO")
        return

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("NO")
            return

    print("YES")

N = int(input())
prime(N)