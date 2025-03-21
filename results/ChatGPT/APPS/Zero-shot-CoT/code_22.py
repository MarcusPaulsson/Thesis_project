def minDigit(x):
    return min(int(d) for d in str(x))

def maxDigit(x):
    return max(int(d) for d in str(x))

def calculate_a_k(a1, K):
    a_n = a1
    for _ in range(K - 1):
        min_digit = minDigit(a_n)
        max_digit = maxDigit(a_n)
        a_n += min_digit * max_digit
    return a_n

t = int(input())
for _ in range(t):
    a1, K = map(int, input().split())
    result = calculate_a_k(a1, K)
    print(result)