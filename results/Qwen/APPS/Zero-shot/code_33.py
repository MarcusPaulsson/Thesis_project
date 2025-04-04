def count_common_terms(a1, b1, a2, b2, L, R):
    count = 0
    x = max(b1, b2)
    while x <= R:
        if (x - b1) % a1 == 0 and (x - b2) % a2 == 0:
            count += 1
        x += 1
    return count

a1, b1, a2, b2, L, R = map(int, input().split())
print(count_common_terms(a1, b1, a2, b2, L, R))