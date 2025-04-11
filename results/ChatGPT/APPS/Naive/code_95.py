def generate_string(n, s, t):
    # Count of each character
    count_a = n
    count_b = n
    count_c = n
    
    # Create a list to hold the result
    res = []
    
    # Function to append characters while avoiding substrings
    def append_char(char):
        nonlocal count_a, count_b, count_c
        if char == 'a' and count_a > 0:
            res.append('a')
            count_a -= 1
        elif char == 'b' and count_b > 0:
            res.append('b')
            count_b -= 1
        elif char == 'c' and count_c > 0:
            res.append('c')
    
    # Try to build the result string
    while count_a > 0 or count_b > 0 or count_c > 0:
        if len(res) >= 1 and ''.join(res[-1:]) == s[0] and count_a > 0:
            append_char('c' if 'c' in s else 'b')
        elif len(res) >= 1 and ''.join(res[-1:]) == s[1] and count_a > 0:
            append_char('c' if 'c' in t else 'a')
        elif len(res) >= 2 and ''.join(res[-2:]) == s:
            append_char('c' if 'c' in s else 'b')
        elif len(res) >= 2 and ''.join(res[-2:]) == t:
            append_char('a' if 'a' in t else 'b')
        else:
            if count_a > 0:
                append_char('a')
            elif count_b > 0:
                append_char('b')
            elif count_c > 0:
                append_char('c')
    
    # Check if we have formed a valid string
    result_str = ''.join(res)
    if s in result_str or t in result_str:
        return "NO"
    
    return "YES", result_str

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

# Generate the string
result = generate_string(n, s, t)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])