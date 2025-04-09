n = int(input())
strings = [input().strip() for _ in range(n)]

# Sort strings by their lengths
strings.sort(key=len)

# Check if the ordering is valid
for i in range(n):
    for j in range(i):
        if strings[j] not in strings[i]:
            print("NO")
            exit()

print("YES")
for s in strings:
    print(s)