from collections import Counter

S = str(input().strip())

cher_counts = Counter(S)

for cher in sorted(cher_counts):
    print(f"{cher} : {cher_counts[cher]}")
    