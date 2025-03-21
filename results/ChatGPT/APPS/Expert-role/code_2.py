def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index].split()))
        index += 1
        b = list(map(int, data[index].split()))
        index += 1
        c = list(map(int, data[index].split()))
        index += 1
        
        p = [0] * n
        
        for i in range(n):
            if i == 0:
                p[i] = a[i]  # Start with the first option
            else:
                # We need to choose a value for p[i] that is not the same as p[i - 1]
                if a[i] != p[i - 1] and (i != n - 1 or a[i] != p[0]):
                    p[i] = a[i]
                elif b[i] != p[i - 1] and (i != n - 1 or b[i] != p[0]):
                    p[i] = b[i]
                else:
                    p[i] = c[i]
        
        # Finally, we need to check the last element with the first element
        if p[n - 1] == p[0]:
            # If they are the same, we can change p[n - 1] to the third option
            for option in (a[n - 1], b[n - 1], c[n - 1]):
                if option != p[n - 2] and option != p[0]:
                    p[n - 1] = option
                    break
        
        results.append(" ".join(map(str, p)))
    
    print("\n".join(results))

solve()