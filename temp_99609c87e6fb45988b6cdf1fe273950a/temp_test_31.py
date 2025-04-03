def can_reorder_strings(n, strings):
    # Sort strings by length
    strings.sort(key=len)
    
    # Check if each string is a substring of the next strings in the sorted list
    for i in range(n):
        for j in range(i + 1, n):
            if strings[i] not in strings[j]:
                print("NO")
                return
    
    print("YES")
    print("\n".join(strings))

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Call the function
can_reorder_strings(n, strings)