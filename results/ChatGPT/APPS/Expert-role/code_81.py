def can_reorder_strings(n, strings):
    # Sort strings by length
    strings.sort(key=len)
    
    # Check if the ordering is valid
    for i in range(1, n):
        found = False
        for j in range(i):
            if strings[j] in strings[i]:
                found = True
                break
        if not found:
            print("NO")
            return
    
    print("YES")
    for s in strings:
        print(s)

# Input reading
n = int(input())
strings = [input().strip() for _ in range(n)]
can_reorder_strings(n, strings)