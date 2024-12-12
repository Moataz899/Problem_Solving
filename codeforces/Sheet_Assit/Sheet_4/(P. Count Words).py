S = input().strip() 

def is_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

count = 0
in_word = False 

for char in S:
    if is_letter(char) and not in_word:
        count += 1
        in_word = True
    elif not is_letter(char):
        in_word = False

print(count)
