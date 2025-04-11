def generate_string(n, s, t):
    # Count of each character
    count_a = count_b = count_c = n
    
    # Create a list to hold the result
    res = []
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden():
        return len(res) >= 2 and (res[-1] + res[-2] == s or res[-1] + res[-2] == t)
    
    # Build the result string
    for _ in range(3 * n):
        for char in 'abc':
            if char == 'a' and count_a > 0:
                res.append(char)
                count_a -= 1
                if not is_forbidden():
                    break
                res.pop()  # Backtrack
                count_a += 1
            elif char == 'b' and count_b > 0:
                res.append(char)
                count_b -= 1
                if not is_forbidden():
                    break
                res.pop()  # Backtrack
                count_b += 1
            elif char == 'c' and count_c > 0:
                res.append(char)
                count_c -= 1
                if not is_forbidden():
                    break
                res.pop()  # Backtrack
                count_c += 1
        else:
            # If we couldn't add any character, it's impossible
            return "NO"
    
    return "YES\n" + ''.join(res)

# Read input
n = int(input())
s = input().strip()
t = input().strip()

# Generate the result
result = generate_string(n, s, t)
print(result)