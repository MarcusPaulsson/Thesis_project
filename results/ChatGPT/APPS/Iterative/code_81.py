def can_rearrange_as_substrings(n, strings):
    # Sort strings by length
    strings.sort(key=len)
    
    # Check if each string is a substring of the next strings
    for i in range(n):
        for j in range(i + 1, n):
            if strings[i] not in strings[j]:
                print("NO")
                return
            
    print("YES")
    print("\n".join(strings))

# Input handling
n = int(input().strip())
strings = [input().strip() for _ in range(n)]
can_rearrange_as_substrings(n, strings)