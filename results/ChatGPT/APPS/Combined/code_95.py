def generate_string(n, s, t):
    # Create a list to hold the result
    res = []
    
    # Count of each character
    counts = {'a': n, 'b': n, 'c': n}
    
    # Function to check if the last two characters in res form a forbidden substring
    def is_forbidden():
        return ''.join(res[-2:]) in (s, t) if len(res) >= 2 else False
    
    # Fill the result while ensuring no forbidden substrings
    while sum(counts.values()) > 0:
        for char in 'abc':
            if counts[char] > 0:
                res.append(char)
                counts[char] -= 1
                
                # Check if the last two characters form a forbidden substring
                if is_forbidden():
                    res.pop()  # Remove the last character added
                    counts[char] += 1  # Restore the count
                else:
                    break  # Valid addition, continue to next character

    # Join the result list into a string
    result_string = ''.join(res)
    
    # Check if the result is valid
    if len(result_string) == 3 * n and not is_forbidden():
        return "YES\n" + result_string
    else:
        return "NO"

# Read input
n = int(input())
s = input().strip()
t = input().strip()

# Generate and print the result
print(generate_string(n, s, t))