def count_common_ap(a1, b1, a2, b2, L, R):
    # Calculate the first term of the two sequences
    start1 = b1
    start2 = b2
    
    # Adjust the start values to be >= L
    if start1 < L:
        if (L - start1) % a1 != 0:
            start1 += (L - start1) // a1 * a1 + a1
        else:
            start1 = L
    
    if start2 < L:
        if (L - start2) % a2 != 0:
            start2 += (L - start2) // a2 * a2 + a2
        else:
            start2 = L
    
    # Identify the maximum possible value to consider
    end1 = R // a1 * a1 + b1
    end2 = R // a2 * a2 + b2
    
    # Store the common terms
    common_terms = set()
    
    # Generate terms of the first arithmetic progression
    for x in range(start1, R + 1, a1):
        if L <= x <= R:
            common_terms.add(x)
    
    # Count the numbers in the second arithmetic progression that are also in the common_terms
    count = 0
    for x in range(start2, R + 1, a2):
        if x in common_terms:
            count += 1
    
    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())

# Get the result
result = count_common_ap(a1, b1, a2, b2, L, R)

# Print the result
print(result)