def can_transform(s, t):
    # Check if both strings have at least one common character
    return len(set(s) & set(t)) > 0

q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    if can_transform(s, t):
        print("YES")
    else:
        print("NO")