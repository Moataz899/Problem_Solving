id = int(input())

row = id // 4
if row % 2 == 0 :
    column = id % 4
else :
    column = 3 - id % 4

print(row, column)
