N, M = map(int, input().split())
A = []

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    
num = int(input())

found = False

for row in A:
    if num in row:
        found = True
        break

if found :
    print("will not take number")
else:
    print("will take number")

