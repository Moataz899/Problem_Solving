A, S, B = input().split()
A = int(A)
B = int(B)
S = str(S)
if (A >= -100 and A <= 100) and (B >= -100 and B <= 100):
    if (S == ">" and A > B) or (S == '=' and A == B):
        print('Right')
    elif S == "<" and A < B:
        print('Right')
    else :
        print('Wrong')
        