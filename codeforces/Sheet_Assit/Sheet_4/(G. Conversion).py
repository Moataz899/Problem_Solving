S = str(input().strip())

new_S = S.replace(',', ' ')

for cher in new_S :
    if cher.isalpha() :
        print(cher.swapcase(), end='')
    else :
        print(cher, end='')