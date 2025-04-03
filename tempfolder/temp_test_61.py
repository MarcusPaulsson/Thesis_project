def find_indices(test_cases):
    results = []
    for n, p in test_cases:
        found = False
        for j in range(1, n - 1):
            if p[j - 1] < p[j] > p[j + 1]:
                results.append(f"YES\n{j} {j + 1} {j + 2}")
                found = True
                break
        if not found:
            results.append("NO")
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    test_cases = []
    
    for i in range(T):
        n = int(data[2 * i + 1])
        p = list(map(int, data[2 * i + 2].split()))
        test_cases.append((n, p))
    
    results = find_indices(test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()