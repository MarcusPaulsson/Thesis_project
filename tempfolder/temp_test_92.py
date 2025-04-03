def can_transform(s, t):
    # Check if both strings have at least one common character
    return bool(set(s) & set(t))

q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    if can_transform(s, t):
        print("YES")
    else:
        print("NO")