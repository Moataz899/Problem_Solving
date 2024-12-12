n = int(input())
a = list(map(int, input().split()))

result = []

while a:
    result.append(a.pop(0))
    if a :
        result.append(a.pop())
        
print(*result)