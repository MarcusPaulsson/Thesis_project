n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
max_a = max(a)

if min_a == max_a:
    print(0)
else:
    difference = max_a - min_a
    print(difference // 2 if difference % 2 == 0 else -1)