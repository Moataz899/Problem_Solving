A, S1, B, S2, output = input().split()

A = int(A)
B = int(B)
output = int(output)

if S1 == "+":
    result = A + B
elif S1 == "-":
    result = A - B
elif S1 == "*":
    result = A * B

if -100 <= A <= 100 and -100 <= B <= 100 or -10**5 <= output <= 10**5:
    print("Yes" if result == output else result)

