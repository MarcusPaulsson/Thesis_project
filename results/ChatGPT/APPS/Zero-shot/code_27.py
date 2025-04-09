n = int(input())
s = input()

min_operations = n

for i in range(1, n):
    if s[:i] == s[i:2*i]:
        min_operations = min(min_operations, i + (n - 2 * i) + 1)

print(min(min_operations, n))