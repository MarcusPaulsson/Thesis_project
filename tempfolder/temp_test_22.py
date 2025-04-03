def min_digit(x):
    return min(int(d) for d in str(x))

def max_digit(x):
    return max(int(d) for d in str(x))

def calculate_a_k(a1, k):
    for _ in range(k):
        a1 += min_digit(a1) * max_digit(a1)
    return a1

t = int(input())
results = []
for _ in range(t):
    a1, k = map(int, input().split())
    results.append(calculate_a_k(a1, k))

print("\n".join(map(str, results)))