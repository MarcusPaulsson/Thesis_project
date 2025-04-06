def max_painted_sections(n, q, painters):
    painted = [0] * (n + 1)
    
    for l, r in painters:
        for i in range(l, r + 1):
            painted[i] += 1
            
    total_sections = sum(1 for i in range(1, n + 1) if painted[i] > 0)
    
    max_painted = 0
    
    for i in range(q):
        # Create a copy of painted sections
        painted_copy = painted[:]
        
        # Remove the influence of the i-th painter
        l, r = painters[i]
        for j in range(l, r + 1):
            painted_copy[j] -= 1
            
        # Count how many sections are still painted
        sections = sum(1 for k in range(1, n + 1) if painted_copy[k] > 0)
        
        # We want to maximize the painted sections
        max_painted = max(max_painted, sections)
    
    return max_painted

# Read input
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output the result
print(max_painted_sections(n, q, painters))