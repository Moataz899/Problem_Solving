import sys
input = sys.stdin.read

def range_sum(L, R):
    if L > R:
        L, R = R, L  
    return (R * (R + 1) // 2) - (L * (L - 1) // 2)

def main():
    data = input().split()
    T = int(data[0])
    results = []
    idx = 1
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx + 1])
        results.append(str(range_sum(L, R)))
        idx += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
