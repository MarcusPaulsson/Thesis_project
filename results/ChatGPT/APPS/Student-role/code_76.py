t = int(input())
results = []

for _ in range(t):
    n = int(input())
    if n % 4 == 0 or n % 4 == 2:
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))