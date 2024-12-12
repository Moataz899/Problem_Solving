N = int(input())
A = list(map(int, input().split()))

min_element = min(A)

frequency = A.count(min_element)

if frequency % 2 == 1:
    print("Lucky")
else:
    print("Unlucky")
    
    