def can_reorder_strings(n, strings):
    # Sort strings by length first, then alphabetically for stability
    strings.sort(key=lambda x: (len(x), x))
    
    # Check if each string is a substring of the next one
    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"
    
    result = "YES\n" + "\n".join(strings)
    return result

# Input handling
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the result
result = can_reorder_strings(n, strings)

# Print the result
print(result)