def can_reorder_strings(strings):
    # Sort strings by their lengths
    strings.sort(key=len)
    
    # Check if the order is valid
    for i in range(len(strings)):
        for j in range(i):
            if strings[j] not in strings[i]:
                return "NO"
    
    # If valid, return the ordered strings
    return "YES", strings

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the result
result = can_reorder_strings(strings)

# Print the result
if result == "NO":
    print(result)
else:
    print(result[0])
    for s in result[1]:
        print(s)