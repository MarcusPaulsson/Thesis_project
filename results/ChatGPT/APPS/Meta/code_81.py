n = int(input())
strings = [input().strip() for _ in range(n)]

# Sort strings by length
strings.sort(key=len)

# Check for substring condition
for i in range(n):
    for j in range(i):
        if strings[j] not in strings[i]:
            print("NO")
            exit()

print("YES")
for string in strings:
    print(string)