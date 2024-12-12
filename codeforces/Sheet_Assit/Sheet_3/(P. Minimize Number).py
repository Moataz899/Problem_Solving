N = int(input())

A = list(map(int, input().split()))

oper = 0

while all(a % 2 == 0 for a in A):
    
    A = [a // 2 for a in A]
    
    oper += 1

print(oper)
