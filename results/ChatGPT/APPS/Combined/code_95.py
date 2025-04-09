def generate_string(n, s, t):
    # Create the base string with n 'a's, n 'b's, and n 'c's
    base = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Check for forbidden pairs
    forbidden_pairs = {s, t}

    # Function to check if the last two characters form a forbidden pair
    def ends_with_forbidden(pair):
        return pair in forbidden_pairs

    # Construct the result string
    result = []
    for char in base:
        result.append(char)
        # If the last two characters form a forbidden pair, skip the next character
        if len(result) >= 2 and ends_with_forbidden(''.join(result[-2:])):
            # Find a valid character to replace the last character
            for replacement in 'abc':
                if replacement != char and (len(result) < 2 or not ends_with_forbidden(''.join(result[-2:] + [replacement]))):
                    result[-1] = replacement
                    break

    # Join the result and check if it contains forbidden substrings
    result_str = ''.join(result)
    if any(f in result_str for f in forbidden_pairs):
        return "NO", None

    return "YES", result_str

# Reading input
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generating the result
result = generate_string(n, s, t)

# Print the output
print(result[0])
if result[0] == "YES":
    print(result[1])