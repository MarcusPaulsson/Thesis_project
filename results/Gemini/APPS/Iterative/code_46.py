n, m = map(int, input().split())
count = 0
for i in range(1, 6):
    count += (n + 5 - i) // 5 * ((m + i - 1) // 5)
print(count)