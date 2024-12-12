N, A, B = map(int, input().split())

sum = 0

for i in range(1, N + 1):
    digit_sum = 0
    temp = i
    
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
        
    if A <= digit_sum <= B :
        sum += i     

print(sum)   
