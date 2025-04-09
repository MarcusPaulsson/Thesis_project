def is_s_palindrome(s: str) -> str:
    # Define a mapping for reflective symmetry
    reflection_map = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 
        'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 
        'Y': 'Y', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'
    }
    
    n = len(s)
    # Check each character in the first half of the string
    for i in range((n + 1) // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        # Verify if characters reflect correctly
        if reflection_map.get(left_char) != right_char:
            return "NIE"
    
    return "TAK"

# Read input
s = input().strip()
# Print output
print(is_s_palindrome(s))