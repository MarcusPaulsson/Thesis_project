def generate_string(n, s, t):
    # Create a base list with n 'a's, n 'b's, and n 'c's
    base_list = ['a'] * n + ['b'] * n + ['c'] * n

    # Function to check if the last two characters form a forbidden substring
    def is_forbidden(last_two):
        return last_two in {s, t}

    # Attempt to construct a valid string
    result = []
    for char in base_list:
        if len(result) >= 1 and is_forbidden(result[-1] + char):
            # If appending this char leads to a forbidden substring, try to find a different char
            for alternate in base_list:
                if alternate != char and not is_forbidden(result[-1] + alternate):
                    result.append(alternate)
                    base_list.remove(alternate)
                    break
            else:
                # If no valid alternate found, return "NO"
                return "NO"
        else:
            result.append(char)

    return "YES\n" + ''.join(result)

# Input reading
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate and print the result
result = generate_string(n, s, t)
print(result)