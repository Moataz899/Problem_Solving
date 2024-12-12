def Average(*args):
    return sum(*args) /len(*args)

N = int(input())
A = list(map(float, input().split()))

Mean = Average(A)
print(f"{Mean:.6f}")