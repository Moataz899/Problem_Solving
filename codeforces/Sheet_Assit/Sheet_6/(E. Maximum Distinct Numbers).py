N = int(input())

sum_max = 0
sum_numbers = 0

while sum_numbers <= N :
    sum_max += 1
    sum_numbers += sum_max

print(sum_max - 1)