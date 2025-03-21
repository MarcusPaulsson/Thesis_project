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
        b = list(map(int, data[index + 2].split()))
        c = list(map(int, data[index + 3].split()))
        index += 4
        
        p = [0] * n
        
        for i in range(n):
            # Choose the first option
            chosen = a[i]
            if i > 0 and chosen == p[i - 1]:
                # If it's the same as the previous one, choose the second option
                chosen = b[i] if b[i] != p[i - 1] else c[i]
            p[i] = chosen
        
        # Handle the case for the last element to ensure it's not the same as the first
        if p[n - 1] == p[0]:
            # If it is the same, we need to change it
            if n > 1:
                # Change to either b[n-1] or c[n-1] that is not p[n-2] and p[0]
                if b[n - 1] != p[n - 2] and b[n - 1] != p[0]:
                    p[n - 1] = b[n - 1]
                else:
                    p[n - 1] = c[n - 1]
        
        results.append(' '.join(map(str, p)))
    
    print('\n'.join(results))

# Run the function
solve()