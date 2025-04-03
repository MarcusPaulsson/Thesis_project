def can_reorder_strings(strings):
    # Sort strings by length
    strings.sort(key=len)
    
    for i in range(1, len(strings)):
        # Check if the current string is a substring of the next one
        if strings[i-1] not in strings[i]:
            return "NO"
    
    return "YES\n" + "\n".join(strings)

# Input reading
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the result and print it
result = can_reorder_strings(strings)
print(result)