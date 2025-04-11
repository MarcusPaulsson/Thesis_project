def can_reorder_strings(strings):
    # Sort strings by their lengths
    strings.sort(key=len)
    
    # Check if each string is a substring of the next one
    for i in range(len(strings) - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"
    
    return "YES", strings

# Read input
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Get the result
result = can_reorder_strings(strings)

# Print the result
if result == "NO":
    print(result)
else:
    print(result[0])
    for string in result[1]:
        print(string)