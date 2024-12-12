T = int(input())

for i in range(T):
    S = str(input())
    
    if "010" in S or "101" in S :
        print("Good")
    else :
        print("Bad")
