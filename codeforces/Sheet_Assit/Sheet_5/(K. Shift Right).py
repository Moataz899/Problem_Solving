def shit_right(arr, x):
    n = len(arr)
    x = x % N
    return arr[-x:] + arr[:-x]

N, X = map(int, input().split())
arr = list(map(int, input().split()))

print(*shit_right(arr, X))
