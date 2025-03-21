def min_digit(x):
    return min(int(d) for d in str(x))

def max_digit(x):
    return max(int(d) for d in str(x))

def calculate_a_k(a1, k):
    a_n = a1
    for _ in range(k - 1):
        min_d = min_digit(a_n)
        max_d = max_digit(a_n)
        a_n += min_d * max_d
    return a_n

t = int(input())
for _ in range(t):
    a1, k = map(int, input().split())
    result = calculate_a_k(a1, k)
    print(result)