def distribute_gifts(test_cases):
    results = []
    for n, a, b in test_cases:
        # Sort both arrays
        a.sort()
        b.sort()
        
        # Create a result where we offset the bracelet by a fixed amount
        # to ensure distinct sums
        offset = 1001  # A value greater than any possible sum
        b_offset = [x + offset for x in b]  # Offset the bracelet values
        
        results.append((a, b_offset))
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1].split()))
        b = list(map(int, data[index + 2].split()))
        test_cases.append((n, a, b))
        index += 3
    
    results = distribute_gifts(test_cases)
    
    for a, b in results:
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

if __name__ == "__main__":
    main()