def can_reorder_strings(n, strings):
    # Sort strings by length
    strings.sort(key=len)
    
    for i in range(n):
        for j in range(i):
            if strings[j] not in strings[i]:
                print("NO")
                return
    
    print("YES")
    for s in strings:
        print(s)

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

can_reorder_strings(n, strings)