A, B = map(int, input().split())

found_lucky = False 

for i in range(A, B + 1):
    if all(char in '47' for char in str(i)):
        print(i, end = ' ')
        found_lucky = True
        
    
if not found_lucky :
    print(-1)