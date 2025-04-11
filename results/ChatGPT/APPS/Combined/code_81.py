def can_reorder_strings(n, strings):
    # Step 1: Sort strings by their lengths
    strings.sort(key=len)

    # Step 2: Check if each string is a substring of the next one
    for i in range(n - 1):
        if strings[i] not in strings[i + 1]:
            return "NO"

    # Step 3: If all checks passed, return the result
    return "YES", strings

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the result
result = can_reorder_strings(n, strings)

# Print the output
if result == "NO":
    print(result)
else:
    print(result[0])
    print('\n'.join(result[1]))