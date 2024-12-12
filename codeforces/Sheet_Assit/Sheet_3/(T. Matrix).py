N = int(input())

primary_diag = 0
secondary_diag = 0

for i in range(N):
    row = list(map(int, input().split()))
    
    primary_diag += row[i]
    secondary_diag += row[N - 1 - i]

print(abs(primary_diag - secondary_diag))


