def maximize_painted_sections(n, q, painters):
    total_sections = [0] * (n + 2)
    
    for l, r in painters:
        total_sections[l] += 1
        total_sections[r + 1] -= 1

    # Calculate the number of painted sections if all painters are hired
    painted_sections = [0] * (n + 1)
    current_paint = 0
    for i in range(1, n + 1):
        current_paint += total_sections[i]
        painted_sections[i] = current_paint

    # Calculate the painted sections count
    painted_count = sum(1 for i in range(1, n + 1) if painted_sections[i] > 0)

    # Now to find the maximum sections painted by hiring q - 2 painters
    max_painted = 0

    for i in range(q):
        l1, r1 = painters[i]
        # Temporarily remove the effect of painter i
        temp_sections = painted_sections[:]
        
        for j in range(l1, r1 + 1):
            temp_sections[j] -= 1

        # Re-calculate painted sections without painter i
        current_count = sum(1 for k in range(1, n + 1) if temp_sections[k] > 0)
        
        for j in range(i + 1, q):
            l2, r2 = painters[j]
            # Temporarily remove the effect of painter j
            temp_sections2 = temp_sections[:]
            
            for k in range(l2, r2 + 1):
                temp_sections2[k] -= 1

            # Re-calculate painted sections without painter i and j
            current_count2 = sum(1 for k in range(1, n + 1) if temp_sections2[k] > 0)
            max_painted = max(max_painted, current_count2)

    return max(max_painted, painted_count)

# Input reading
n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# Output result
print(maximize_painted_sections(n, q, painters))