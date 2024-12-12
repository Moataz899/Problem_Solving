n = int(input())
a = list(map(int, input().split()))
ouput = []
for i in range(n):
    if a[i] == 0:
        ouput = ouput[::-1]
    ouput.append(a[i])

print(*ouput)
