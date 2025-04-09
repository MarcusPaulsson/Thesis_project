def count_common_terms(a1, b1, a2, b2, L, R):
    def count_terms(a, b, start, end):
        if a == 0:
            return 1 if start <= b <= end else 0
        
        # Calculate the first term in the range
        first_term = max(b, start + (a - (start - b) % a) % a)
        # Calculate the last term in the range
        last_term = min(end, b + ((end - b) // a) * a)
        
        if first_term > last_term:
            return 0
        
        return (last_term - first_term) // a + 1
    
    count1 = count_terms(a1, b1, L, R)
    count2 = count_terms(a2, b2, L, R)

    count_common = 0
    
    for k in range(count1):
        x = a1 * k + b1
        if L <= x <= R:
            # Check if x can be represented in the second progression
            if (x - b2) % a2 == 0 and (x - b2) // a2 >= 0:
                count_common += 1

    return count_common

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_terms(a1, b1, a2, b2, L, R))