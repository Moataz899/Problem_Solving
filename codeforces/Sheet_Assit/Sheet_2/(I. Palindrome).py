N = input().strip()

reversed = str(int(N[::-1]))

print(reversed)

if N == reversed :
    print("Yes")
else :
    print("No")
    