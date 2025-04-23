def can_reorder_strings(n, strings):
    # Sort strings by length and then lexicographically
    strings.sort(key=lambda x: (len(x), x))
    
    # Check if each string is a substring of the next one
    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"
    
    return "YES", strings

# Input reading
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Get the result
result = can_reorder_strings(n, strings)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print("\n".join(result[1]))