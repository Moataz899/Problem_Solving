N, K = map(int, input().split())

numbers = list(map(int, input().split()))

result = []

for i in range(0, N, K):
    
    result.append(min(numbers[i:i+K]))

print(" ".join(map(str, result)))
  