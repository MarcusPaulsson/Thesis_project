def can_reorder_strings(n, strings):
    # Sort strings by length first, then lexicographically
    strings.sort(key=lambda x: (len(x), x))
    
    # Check if each string is a substring of the next one
    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"
    
    return "YES\n" + "\n".join(strings)

# Input reading
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get result and print
result = can_reorder_strings(n, strings)
print(result)