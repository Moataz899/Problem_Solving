# Case 1 
N = int(input())

for i in range(1, N + 1 ):
    if N % i == 0 :
        print(i)
        
# Case 2
def print_dividsors(N):
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)
            
I = int(input())

print_dividsors(I)
