def secure_ski_resort(test_cases):
    results = []
    
    for n, m, tracks in test_cases:
        # We can just pick the last n//2 spots to close as a simple solution
        spots_to_close = []
        
        # We can close the last n//2 spots (if n is odd, we close (n//2)+1 spots)
        for i in range((n + 1) // 2, n + 1):
            spots_to_close.append(i)
        
        results.append((len(spots_to_close), spots_to_close))
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(T):
        n, m = map(int, data[index].split())
        index += 1
        tracks = []
        for __ in range(m):
            x, y = map(int, data[index].split())
            tracks.append((x, y))
            index += 1
        test_cases.append((n, m, tracks))
    
    results = secure_ski_resort(test_cases)
    
    for k, spots in results:
        print(k)
        print(" ".join(map(str, spots)))

if __name__ == "__main__":
    main()