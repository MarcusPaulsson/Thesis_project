def count_valid_pairs(l, r):
    count = 0
    for a in range(l, r + 1):
        for b in range(l, r + 1):
            if a + b == a ^ b:
                count += 1
    return count

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    result = count_valid_pairs(l, r)
    print(result)