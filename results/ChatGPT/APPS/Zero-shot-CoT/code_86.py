def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1].split()))
        index += 2
        
        count_0 = a.count(0)
        count_1 = a.count(1)
        
        if count_0 >= n // 2:
            # We can keep n//2 zeros
            results.append(f"{count_0}")
            results.append(" ".join(["0"] * (n // 2)))
        elif count_1 >= n // 2:
            # We can keep n//2 ones
            results.append(f"{count_1}")
            results.append(" ".join(["1"] * (n // 2)))
        else:
            # We can keep n//2 of each
            results.append(f"{n}")
            results.append(" ".join(map(str, a)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()