n = int(input())
strings = [input().strip() for _ in range(n)]

# Sort strings by length
strings.sort(key=len)

# Check if the order is valid
for i in range(1, n):
    if strings[i-1] not in strings[i]:
        print("NO")
        break
else:
    print("YES")
    print("\n".join(strings))