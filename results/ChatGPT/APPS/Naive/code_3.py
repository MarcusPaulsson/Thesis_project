def max_painted_sections(n, q, painters):
    # Create a list to store the coverage for each section
    covered = [0] * (n + 1)
    
    # Count the initial coverage for each section
    for l, r in painters:
        for i in range(l, r + 1):
            covered[i] += 1
    
    # Calculate the max painted sections with combinations of excluding two painters
    max_sections = 0
    
    for i in range(q):
        for j in range(i + 1, q):
            # Create a temporary coverage list
            temp_covered = covered[:]
            
            # Exclude the i-th and j-th painter
            l_i, r_i = painters[i]
            l_j, r_j = painters[j]
            
            for index in range(l_i, r_i + 1):
                temp_covered[index] -= 1
            for index in range(l_j, r_j + 1):
                temp_covered[index] -= 1
            
            # Count the painted sections
            painted_sections = sum(1 for x in range(1, n + 1) if temp_covered[x] > 0)
            max_sections = max(max_sections, painted_sections)
    
    return max_sections

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Get the result and print it
result = max_painted_sections(n, q, painters)
print(result)