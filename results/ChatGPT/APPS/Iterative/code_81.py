def can_reorder_strings(n, strings):
    # Sort the strings by their lengths
    strings.sort(key=len)

    # Check if the ordering works
    for i in range(1, n):
        if strings[i-1] not in strings[i]:
            print("NO")
            return

    print("YES")
    for string in strings:
        print(string)

# Read input
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Process and print the result
can_reorder_strings(n, strings)