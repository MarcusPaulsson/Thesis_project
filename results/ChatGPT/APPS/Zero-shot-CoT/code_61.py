def find_indices(test_cases):
    result = []
    for n, p in test_cases:
        found = False
        for j in range(1, n-1):
            if p[j-1] < p[j] > p[j+1]:
                result.append(f"YES\n{j} {j+1} {j+2}")
                found = True
                break
        if not found:
            result.append("NO")
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
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