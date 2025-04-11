n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

coloring = [0] * n
frequency = defaultdict(list)

for index, value in enumerate(a):
    frequency[value].append(index)

if len(frequency) > k:
    print("NO")
else:
    print("YES")
    color = 1
    for indices in frequency.values():
        for i in range(len(indices)):
            coloring[indices[i]] = (i % k) + 1
    print(" ".join(map(str, coloring)))