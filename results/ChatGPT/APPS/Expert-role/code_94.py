def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, T = int(data[index]), int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        
        color = [0] * n
        count = defaultdict(int)
        
        for i in range(n):
            count[a[i]] += 1
        
        for i in range(n):
            complement = T - a[i]
            if complement in count:
                if count[complement] > 0:
                    if a[i] == complement:
                        # Handle the case where a[i] == complement
                        if count[a[i]] > 1:
                            color[i] = 1
                            count[a[i]] -= 1
                        else:
                            color[i] = 0
                    else:
                        # Assign colors based on the availability of pairs
                        if count[complement] > 0:
                            color[i] = 0
                            count[complement] -= 1
                            count[a[i]] -= 1
                        else:
                            color[i] = 1
            else:
                color[i] = 0
            
        results.append(" ".join(map(str, color)))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()