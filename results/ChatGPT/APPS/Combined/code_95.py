def generate_string(n, s, t):
    # Initialize counts for 'a', 'b', and 'c'
    counts = {'a': n, 'b': n, 'c': n}
    
    # Create a list to build the result string
    res = []
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden():
        return ''.join(res[-2:]) in (s, t) if len(res) >= 2 else False
    
    # Build the result string while avoiding forbidden substrings
    while sum(counts.values()) > 0:
        for char in 'abc':
            if counts[char] > 0:
                res.append(char)
                counts[char] -= 1
                if is_forbidden():
                    res.pop()
                    counts[char] += 1
                else:
                    break
        else:
            # If we couldn't add any character, it means we are stuck
            return "NO", ""
    
    # Check if the result is valid
    return "YES", ''.join(res)

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

# Generate the result
result = generate_string(n, s, t)

# Output the result
print(result[0])
if result[0] == "YES":
    print(result[1])