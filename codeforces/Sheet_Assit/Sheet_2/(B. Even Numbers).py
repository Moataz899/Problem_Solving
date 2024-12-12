N = int(input())

floage = False
for i in range(2, N+1):
    if i % 2 == 0:
        print(i)
        floage = True
        
if not floage :
    print(-1)
