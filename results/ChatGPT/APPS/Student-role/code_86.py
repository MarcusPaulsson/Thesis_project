def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1].split()))
        index += 2
        
        count_0 = a.count(0)
        count_1 = a.count(1)
        
        if count_0 % 2 == 0 and count_0 > 0:
            results.append(f"{count_0}")
            results.append(" ".join("0" for _ in range(count_0)))
        elif count_1 % 2 == 0 and count_1 > 0:
            results.append(f"{count_1}")
            results.append(" ".join("1" for _ in range(count_1)))
        else:
            if count_0 > 0:
                results.append(f"{count_0 - 1}")
                results.append(" ".join("0" for _ in range(count_0 - 1)))
            else:
                results.append(f"{count_1 - 1}")
                results.append(" ".join("1" for _ in range(count_1 - 1)))

    print("\n".join(results))

solve()