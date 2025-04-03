def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx].split()))
        idx += 1
        
        count_0 = a.count(0)
        count_1 = a.count(1)

        if count_0 >= n // 2:
            # Enough zeros to satisfy the condition
            result = [0] * (n // 2)
        else:
            # We have more ones, we can only take enough ones to balance
            result = [1] * (n // 2)

        results.append(f"{len(result)}")
        results.append(" ".join(map(str, result)))

    print("\n".join(results))

if __name__ == "__main__":
    solve()