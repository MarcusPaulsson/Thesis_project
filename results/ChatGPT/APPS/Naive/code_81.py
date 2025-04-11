def can_reorder_strings(n, strings):
    # Sort strings by length, then lexicographically
    strings.sort(key=lambda x: (len(x), x))
    
    for i in range(1, n):
        # Check if the previous string is a substring of the current string
        if strings[i-1] not in strings[i]:
            return "NO"
    
    return "YES", strings

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the result
result = can_reorder_strings(n, strings)

# Print the result
if result == "NO":
    print(result)
else:
    print(result[0])
    for string in result[1]:
        print(string)