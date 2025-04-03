def generate_string(n, s, t):
    # Count of each character
    count_a = n
    count_b = n
    count_c = n

    # Create a list to build the result
    res = []

    # Helper function to check if the last two characters form a forbidden substring
    def is_forbidden():
        return ''.join(res[-2:]) == s or ''.join(res[-2:]) == t

    # While there are characters left to add
    while count_a > 0 or count_b > 0 or count_c > 0:
        for char in 'abc':
            if char == 'a' and count_a > 0:
                res.append('a')
                count_a -= 1
            elif char == 'b' and count_b > 0:
                res.append('b')
                count_b -= 1
            elif char == 'c' and count_c > 0:
                res.append('c')
                count_c -= 1

            # Check if the last two characters form a forbidden substring
            if is_forbidden():
                # Remove the last character and continue to the next
                res.pop()
                if char == 'a': count_a += 1
                elif char == 'b': count_b += 1
                elif char == 'c': count_c += 1

            # If we have filled the result with 3n characters, break
            if len(res) == 3 * n:
                break
        else:
            # If we didn't break out, we reached a point where we can't add anything more
            break

    # Check if we constructed a valid string
    if len(res) == 3 * n:
        print("YES")
        print(''.join(res))
    else:
        print("NO")

# Read inputs
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate the string
generate_string(n, s, t)