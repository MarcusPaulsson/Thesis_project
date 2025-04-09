def generate_string(n, s, t):
    # Create a list that will hold the result
    res = []
    
    # Characters count
    count = {'a': n, 'b': n, 'c': n}
    
    # Function to check if last two characters form a forbidden substring
    def is_forbidden(last_two):
        return last_two == s or last_two == t
    
    # Fill the result string
    for _ in range(3 * n):
        for char in 'abc':
            if count[char] > 0:
                # Check if adding this character would create a forbidden substring
                if len(res) >= 2 and is_forbidden(res[-2] + char):
                    continue
                # Append the character and decrease the count
                res.append(char)
                count[char] -= 1
                break
        else:
            # If we couldn't add any character, then it means it's impossible
            return "NO", ""
    
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