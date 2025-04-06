a, b, c = map(int, input().split())

if c == 0:
    print("YES" if a == b else "NO")
else:
    is_reachable = (b - a) % c == 0 and (b - a) // c >= 0
    print("YES" if is_reachable else "NO")