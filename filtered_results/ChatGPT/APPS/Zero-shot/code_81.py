def can_reorder_as_substrings(n, strings):
    # Sort the strings by their lengths
    strings.sort(key=len)
    
    # Check if each string is a substring of the next strings in the list
    for i in range(n):
        for j in range(i + 1, n):
            if strings[i] not in strings[j]:
                print("NO")
                return
    
    print("YES")
    for s in strings:
        print(s)

# Input reading
n = int(input())
strings = [input().strip() for _ in range(n)]

# Call the function
can_reorder_as_substrings(n, strings)