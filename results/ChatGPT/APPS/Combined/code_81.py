def can_reorder_strings(n, strings):
    # Sort strings by their lengths
    strings.sort(key=len)
    
    # Check if each string is a substring of the next one
    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"
    
    # Return the ordered strings
    return "YES", strings

# Input handling
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Process the strings and output the result
result = can_reorder_strings(n, strings)
if result == "NO":
    print(result)
else:
    print(result[0])
    print("\n".join(result[1]))