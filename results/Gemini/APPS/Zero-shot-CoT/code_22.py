def minDigit(x):
    s = str(x)
    min_digit = 9
    for digit in s:
        min_digit = min(min_digit, int(digit))
    return min_digit

def maxDigit(x):
    s = str(x)
    max_digit = 0
    for digit in s:
        max_digit = max(max_digit, int(digit))
    return max_digit

def solve():
    a1, k = map(int, input().split())
    a = a1
    for i in range(1, int(min(k, 100001))):
        min_d = minDigit(a)
        max_d = maxDigit(a)
        if min_d == 0:
            break
        a = a + min_d * max_d
    print(a)

t = int(input())
for _ in range(t):
    solve()