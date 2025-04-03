def count_valid_pairs(l, r):
    # Count pairs (a, b) such that a + b = a ⊕ b
    # This is true when there are no carry bits in the binary addition of a and b.
    # This condition holds true when (a & b) == 0
    count = 0
    for a in range(l, r + 1):
        # Count how many b's can be paired with this a
        count += (r - l + 1) - bin(a).count('1')
    return count

t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    results.append(count_valid_pairs(l, r))

for result in results:
    print(result)