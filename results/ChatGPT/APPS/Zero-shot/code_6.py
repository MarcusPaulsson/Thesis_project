def process_test_case(n, m, tracks):
    # Use a simple strategy: close the last two spots
    to_close = []
    
    # We can safely close the last two spots if n > 1
    if n > 1:
        to_close = [n, n-1]
    
    # If n is 1, we cannot close any spots
    k = len(to_close)
    return k, to_close

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n, m = map(int, data[index].split())
        index += m + 1  # Skip the m lines of tracks
        
        k, to_close = process_test_case(n, m, [])
        results.append(f"{k}")
        if k > 0:
            results.append(" ".join(map(str, to_close)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()