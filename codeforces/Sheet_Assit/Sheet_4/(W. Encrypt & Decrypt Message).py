def transform_string(s, from_str, to_str):
    return "".join([to_str[from_str.index(char)] if char in from_str else char for char in s])

key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

Q = int(input().strip())
S = input().strip()

if Q == 1:
    print(transform_string(S, original, key))
elif Q == 2:
    print(transform_string(S, key, original))
    