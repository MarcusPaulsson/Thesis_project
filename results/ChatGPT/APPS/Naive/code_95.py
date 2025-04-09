def generate_string(n, s, t):
    # Initialize the counts for 'a', 'b', and 'c'
    count_a = count_b = count_c = n

    # Create a list to hold the result characters
    res = []

    # Helper function to check if the last two characters form the substring
    def ends_with(sub):
        return len(res) >= 2 and ''.join(res[-2:]) == sub

    # Fill the result while avoiding substrings s and t
    for _ in range(3 * n):
        for char in 'abc':
            if char == 'a' and count_a > 0:
                if not (ends_with(s) or ends_with(t)):
                    res.append(char)
                    count_a -= 1
                    break
            elif char == 'b' and count_b > 0:
                if not (ends_with(s) or ends_with(t)):
                    res.append(char)
                    count_b -= 1
                    break
            elif char == 'c' and count_c > 0:
                if not (ends_with(s) or ends_with(t)):
                    res.append(char)
                    count_c -= 1
                    break
        else:
            # If we can't add any character, return "NO"
            return "NO", ""

    return "YES", ''.join(res)


# Read input values
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate the result
result = generate_string(n, s, t)
# Print the result
print(result[0])
if result[0] == "YES":
    print(result[1])