T = int(input())

for i in range(T):
    S = str(input())
    
    if len(S) > 10 :
        print(f"{S[0]}{len(S) - 2}{S[-1]}")
        continue
    else :
        print(S)
        
            