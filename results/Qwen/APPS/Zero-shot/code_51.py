from collections import Counter

n = int(input())
divisors = list(map(int, input().split()))

divisor_counts = Counter(divisors)
x_divisors = [d for d, count in divisor_counts.items() if count % 2 == 1]
y_divisors = [d for d, count in divisor_counts.items() if count % 2 == 0]

x = 1
for d in x_divisors:
    x *= d

y = 1
for d in y_divisors:
    y *= d

print(x, y)