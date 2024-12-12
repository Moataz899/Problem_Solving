N, M = map(int, input().split())

A = list(map(int, input().split()))

frequency = [0] * (M + 1)

for num in A:
    frequency[num] += 1

for i in range(1, M + 1):
    print(frequency[i])
