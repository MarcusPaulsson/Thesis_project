n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# If the maximum jump distance d is greater than or equal to n, it's always possible
if d >= n:
    print("YES")
    print("0 " * (n - sum(c)) + " ".join(str(i + 1) for i in range(m) for _ in range(c[i])))
else:
    # Calculate the total length of platforms
    total_length = sum(c)
    
    # Calculate the maximum number of gaps needed
    gaps_needed = m - 1
    
    # Check if we can fit the platforms with the gaps
    if total_length + gaps_needed * d < n:
        print("NO")
    else:
        print("YES")
        result = [0] * n
        position = 0
        
        for i in range(m):
            # Place the platform
            for j in range(c[i]):
                result[position + j] = i + 1
            position += c[i]
            # If it's not the last platform, leave a gap
            if i < m - 1:
                position += d
        
        print(" ".join(map(str, result)))