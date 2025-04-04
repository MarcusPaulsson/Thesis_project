def count_cyclical_strings(n, s):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 2 ** (n // i - len(s) + 1)
    return count

n = int(input())
s = input()
print(count_cyclical_strings(n, s))