def can_construct_string(n, s, t):
    # Create a base string with n 'a's, n 'b's, and n 'c's
    base = 'a' * n + 'b' * n + 'c' * n
    
    # Check if we can find positions to create a valid string
    # We can use a simple approach to rearrange
    for i in range(3):
        for j in range(3):
            if i != j:
                # Create a potential result by interleaving different characters
                res = []
                for k in range(n):
                    res.append(chr(97 + i))  # 'a' + i
                    res.append(chr(97 + j))  # 'a' + j
                res.append(chr(97 + (3 - i - j)))  # add the remaining character
                result = ''.join(res)
                
                # Check if neither s nor t is a substring
                if s not in result and t not in result:
                    return "YES", result
    
    return "NO", ""

# Read input
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate and print the result
result = can_construct_string(n, s, t)
print(result[0])
if result[0] == "YES":
    print(result[1])