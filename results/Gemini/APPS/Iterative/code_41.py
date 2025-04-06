def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    distances = [float('inf')] * n
    
    # Forward pass: find distances to the nearest zero on the left
    last_zero = float('-inf')
    for i in range(n):
        if a[i] == 0:
            last_zero = i
            distances[i] = 0
        elif last_zero != float('-inf'):
            distances[i] = min(distances[i], i - last_zero)
    
    # Backward pass: find distances to the nearest zero on the right
    last_zero = float('inf')
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last_zero = i
            distances[i] = 0
        elif last_zero != float('inf'):
            distances[i] = min(distances[i], last_zero - i)
    
    print(*distances)

solve()