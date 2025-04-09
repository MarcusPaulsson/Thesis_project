def can_reach_end(n, m, d, c):
    # Calculate the total length of platforms
    total_length = sum(c)
    
    # If total length of platforms is less than n, check the jump distance
    if total_length < n:
        # The maximum position we can reach is determined by d
        if d <= 1:
            print("NO")
            return
        # If we can jump more than 1 cell, we can fill the gaps
        # with enough platforms to reach the end
        print("YES")
        # Create the river representation
        river = [0] * n
        position = 0
        
        for i in range(m):
            for j in range(c[i]):
                river[position] = i + 1  # 1-indexed platform
                position += 1
        
        print(" ".join(map(str, river)))
        return

    # If we can jump beyond the width of the river
    print("YES")
    river = [0] * n
    position = 0
    
    for i in range(m):
        for j in range(c[i]):
            river[position] = i + 1  # 1-indexed platform
            position += 1
    
    print(" ".join(map(str, river)))

# Input reading
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

can_reach_end(n, m, d, c)