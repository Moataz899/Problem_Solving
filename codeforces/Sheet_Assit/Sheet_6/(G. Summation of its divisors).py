def sum_of_divisors(n):
    return sum(i + (n // i if i != n // i else 0)
    for i in range(1, int(n**0.5) + 1) if n % i == 0)

N = int(input().strip())
print(sum_of_divisors(N))
