def min_max_digit(n):
    s = str(n)
    min_digit = int(s[0])
    max_digit = int(s[0])
    for digit in s:
        digit = int(digit)
        min_digit = min(min_digit, digit)
        max_digit = max(max_digit, digit)
    return min_digit, max_digit

t = int(input())
for _ in range(t):
    a1, k = map(int, input().split())
    a = a1
    for i in range(1, min(k, 1001)):
        min_digit, max_digit = min_max_digit(a)
        if min_digit == 0:
            break
        a += min_digit * max_digit
    print(a)