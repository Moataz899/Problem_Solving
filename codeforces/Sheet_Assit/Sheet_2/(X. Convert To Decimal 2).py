T = int(input())

for i in range(T):
    n = int(input())
    
    binary = bin(n)
    
    count_ones = binary.count('1')
    
    result = (1 << count_ones) - 1
    
    print(result)
    