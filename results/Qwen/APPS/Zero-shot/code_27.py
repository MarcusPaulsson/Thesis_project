def min_operations(n, s):
    if n == 1:
        return 1
    if s[:n//2] == s[n//2:]:
        return min_operations(n//2, s[:n//2]) + 1
    else:
        return n

n = int(input())
s = input()
print(min_operations(n, s))