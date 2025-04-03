def find_indices(test_cases):
    results = []
    for n, p in test_cases:
        found = False
        for j in range(1, n - 1):
            if p[j - 1] < p[j] > p[j + 1]:
                results.append(f"YES\n{j}\n{j + 1}\n{j + 2}")
                found = True
                break
        if not found:
            results.append("NO")
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(T):
        n = int(data[index])
        p = list(map(int, data[index + 1].split()))
        test_cases.append((n, p))
        index += 2
    
    results = find_indices(test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()