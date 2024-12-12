N = int(input())

for i in range(N):
    S, T = input().split()
    min_len = min(len(S), len(T))
    combined = ''
    
    for j in range(min_len):
        combined += S[j] + T[j]
    
    combined += S[min_len:] + T[min_len:]
    print(combined)
