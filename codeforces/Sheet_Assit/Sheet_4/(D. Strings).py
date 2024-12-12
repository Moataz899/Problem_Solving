A = input()
B = input()

print(len(A), len(B))
print(A + B)

A_Swap = B[0] + A[1:]
B_Swap = A[0] + B[1:]

print(A_Swap, B_Swap)

