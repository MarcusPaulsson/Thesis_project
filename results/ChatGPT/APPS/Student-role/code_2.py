def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
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
                p[i] = a[i]
            else:
                # Choose a value for p[i] that is different from p[i-1]
                if a[i] != p[i-1] and (i != n - 1 or a[i] != b[0]):
                    p[i] = a[i]
                elif b[i] != p[i-1] and (i != n - 1 or b[i] != a[0]):
                    p[i] = b[i]
                else:
                    p[i] = c[i]
        
        # Fix the last element to ensure it is not equal to the first
        if p[n-1] == p[0]:
            if a[n-1] != p[n-2] and a[n-1] != p[0]:
                p[n-1] = a[n-1]
            elif b[n-1] != p[n-2] and b[n-1] != p[0]:
                p[n-1] = b[n-1]
            else:
                p[n-1] = c[n-1]

        results.append(" ".join(map(str, p)))

    print("\n".join(results))

# Call the solve function to execute
solve()