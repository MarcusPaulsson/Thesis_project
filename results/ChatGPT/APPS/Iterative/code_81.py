def can_reorder_strings(n, strings):
    # Sort strings by their lengths
    strings.sort(key=len)

    # Check the substring condition
    for i in range(1, n):
        if not any(strings[j] in strings[i] for j in range(i)):
            return "NO"

    return "YES\n" + "\n".join(strings)

# Read input
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Get the result and print it
print(can_reorder_strings(n, strings))