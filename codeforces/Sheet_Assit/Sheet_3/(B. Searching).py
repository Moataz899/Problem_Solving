N = int(input())

numbers =list(map(int, input().split()))

X = int(input())

for num in range(N):
    if  numbers[num] == X:
        print(num)
        break
else :
    print(-1)
    