n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms and the maximum reachable distance
total_length = sum(c)
max_possible_jump = d * (total_length + 1)

if max_possible_jump < n:
    print("NO")
else:
    print("YES")
    river = [0] * n
    current_position = 0
    
    for platform_index in range(m):
        for _ in range(c[platform_index]):
            if current_position < n:
                river[current_position] = platform_index + 1
                current_position += 1
                
        # Move the current position to the next jumpable area
        if current_position < n:  # Ensure we don't exceed the river length
            current_position += 1

    print(" ".join(map(str, river)))