N = int(input())

numbers = list(map(int, input().split()))

Total_sum = 0

for num in numbers:
    Total_sum += num
    
    if Total_sum < 0:
        Total_sum += abs(num)
        
Total_summation = " ".join(map(str, [Total_sum]))

print(Total_summation)
