N = int(input())

A = list(map(int, input().split()))

lower_num = min(A)

postion_num = A.index(lower_num) + 1

print(lower_num, postion_num)
