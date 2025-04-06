import math

a, b = map(int, input().split())
total = a + b
ans = float('inf')
for h in range(1, int(math.sqrt(total)) + 1):
    if total % h == 0:
        w = total // h
        # Case 1: red forms a rectangle
        for h1 in range(1, int(math.sqrt(a)) + 1):
            if a % h1 == 0:
                w1 = a // h1
                if h1 <= h and w1 <= w:
                    ans = min(ans, 2 * (h + w))
        # Case 2: blue forms a rectangle
        for h2 in range(1, int(math.sqrt(b)) + 1):
            if b % h2 == 0:
                w2 = b // h2
                if h2 <= h and w2 <= w:
                    ans = min(ans, 2 * (h + w))
print(ans)