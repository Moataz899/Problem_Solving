n = int(input())
numbers = list(map(int, input().split()))
max_value = 0

for i in numbers:
    count = 0
    while i % 2 == 0:
        i //= 2
        count += 1
    if count > max_value:
        max_value = count
        
print(max_value)
