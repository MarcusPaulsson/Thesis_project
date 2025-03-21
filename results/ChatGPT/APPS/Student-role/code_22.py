def minDigit(x):
    return min(int(d) for d in str(x))

def maxDigit(x):
    return max(int(d) for d in str(x))

def compute_aK(a1, K):
    a = a1
    for _ in range(K):
        min_d = minDigit(a)
        max_d = maxDigit(a)
        a += min_d * max_d
    return a

t = int(input())
for _ in range(t):
    a1, K = map(int, input().split())
    print(compute_aK(a1, K))