x = int(input())
s = str(x)
n = len(s)
ans = x
max_sum = sum(int(d) for d in s)
for i in range(n):
    if s[i] == '0':
        continue
    num = int(s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1))
    sum_digits = sum(int(d) for d in str(num))
    if sum_digits > max_sum:
        max_sum = sum_digits
        ans = num
    elif sum_digits == max_sum and num > ans:
        ans = num
print(ans)