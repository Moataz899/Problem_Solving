t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    even_count = 0 
    for num in a:
        if num % 2 == 0:
            even_count += 1
    
    odd_count = n - even_count
    
    if n % 2 != 0:
        print(-1)
    else:
        if even_count == odd_count:
            print(0)
        else:
            print(abs(even_count - odd_count) // 2)
