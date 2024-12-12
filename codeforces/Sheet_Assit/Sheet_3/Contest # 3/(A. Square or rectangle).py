t = int(input())

for i in range(t):
    w, h = map(int, input().split())
    
    if w == h :
        print('Square')
    
    elif w > h or w < h:
        print('Rectangle')
    