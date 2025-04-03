def count_common_ap(a1, b1, a2, b2, L, R):
    # Function to find all values in the range [L, R] that can be expressed as both APs
    def count_in_ap(a, b, L, R):
        if a == 0:
            if b < L or b > R:
                return 0
            return (R - L) // a + 1 if L <= R else 0
        
        # Find the first term in the AP that is >= L
        if b < L:
            first = (L - b + a - 1) // a * a + b
        else:
            first = b
        
        # Find the last term in the AP that is <= R
        if b > R:
            last = (R - b) // a * a + b
        else:
            last = b
        
        if first > R or last < L:
            return 0
        
        return (last - first) // a + 1
    
    # Count terms for both APs
    count_a1 = count_in_ap(a1, b1, L, R)
    count_a2 = count_in_ap(a2, b2, L, R)
    
    # Use a set to collect common terms
    common_terms = set()
    
    # Generate terms for the first AP
    for k in range((R - b1) // a1 + 1):
        term = a1 * k + b1
        if L <= term <= R:
            common_terms.add(term)
    
    # Count terms for the second AP and check commonality
    count = 0
    for l in range((R - b2) // a2 + 1):
        term = a2 * l + b2
        if L <= term <= R and term in common_terms:
            count += 1
    
    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Get the result
result = count_common_ap(a1, b1, a2, b2, L, R)
# Print the output
print(result)