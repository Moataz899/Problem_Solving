N = float(input())

if N % 2 == 0 and abs(N - int(N) < 0.1):
    print("int", int(N))
else :
    print(f"float {int(N)} {N - int(N):.3f}")
        