def min_cost_to_break_chocolate(n, m, k):
    # If k equals the total number of squares, no break is needed
    if k == n * m:
        return 0
    
    # The maximum possible size of dp table
    dp = [[float('inf')] * (n * m + 1) for _ in range(n + 1)]
    
    # Base case: 0 cost to eat 0 squares
    dp[0][0] = 0
    
    # Fill dp table
    for width in range(1, n + 1):
        for height in range(1, m + 1):
            total_squares = width * height
            
            # Calculate minimum cost for each possible square count
            for squares in range(1, total_squares + 1):
                # If we can take the whole piece
                if squares == total_squares:
                    dp[width][squares] = 0
                
                # Try horizontal cuts
                for h in range(1, height):
                    cost = width * width  # Breaking cost
                    # Left part
                    left_squares = width * h
                    # Right part
                    right_squares = total_squares - left_squares
                    
                    # Update dp for both parts
                    for left in range(0, squares + 1):
                        if left <= left_squares:
                            right = squares - left
                            if right <= right_squares:
                                dp[width][squares] = min(dp[width][squares], 
                                                          dp[width][left] + dp[width][right] + cost)
                
                # Try vertical cuts
                for w in range(1, width):
                    cost = height * height  # Breaking cost
                    # Top part
                    top_squares = w * height
                    # Bottom part
                    bottom_squares = total_squares - top_squares
                    
                    # Update dp for both parts
                    for top in range(0, squares + 1):
                        if top <= top_squares:
                            bottom = squares - top
                            if bottom <= bottom_squares:
                                dp[width][squares] = min(dp[width][squares], 
                                                          dp[top][height] + dp[bottom][height] + cost)
    
    return dp[n][k]

t = int(input())
results = []
for _ in range(t):
    n, m, k = map(int, input().split())
    results.append(min_cost_to_break_chocolate(n, m, k))

print('\n'.join(map(str, results)))