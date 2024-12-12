def New_Array(A1, A2):
    List = list(A2+ A1)
    
    return List

N = int(input())
List_1 = list(map(int, input().split()))
List_2 = list(map(int, input().split()))

new_array = New_Array(List_1, List_2)

print(*new_array)