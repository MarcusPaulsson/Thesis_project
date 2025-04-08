def max_permutation_not_exceeding(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Sort the digits of a in descending order
    sorted_digits = sorted(a_str, reverse=True)
    
    # Function to find the largest permutation <= b
    def backtrack(current, remaining):
        if len(current) == len(a_str):
            num = int(''.join(current))
            return num if num <= b else -1
        
        max_number = -1
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            
            next_digit = remaining[i]
            next_remaining = remaining[:i] + remaining[i + 1:]
            
            if not current and next_digit == '0':
                continue
            
            candidate = backtrack(current + [next_digit], next_remaining)
            max_number = max(max_number, candidate)
        
        return max_number
    
    return backtrack([], sorted_digits)

# Input Reading
a = int(input().strip())
b = int(input().strip())

# Output the result
print(max_permutation_not_exceeding(a, b))