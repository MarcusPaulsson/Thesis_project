def can_transform(a, b):
    n = len(a)
    can_increase = False
    can_decrease = False

    for i in range(n):
        if a[i] == 1:
            can_increase = True
        elif a[i] == -1:
            can_decrease = True

        if b[i] > a[i] and not can_increase:
            return "NO"
        if b[i] < a[i] and not can_decrease:
            return "NO"

    return "YES"

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = can_transform(a, b)
    results.append(result)

print("\n".join(results))