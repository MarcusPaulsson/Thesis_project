n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

max_number = list(a)  # Start with the original number as a list of characters
i = 0

while i < n:
    if f[int(a[i]) - 1] > int(a[i]):
        # Start replacing if f(x) is greater than x
        while i < n and f[int(a[i]) - 1] >= int(a[i]):
            max_number[i] = str(f[int(a[i]) - 1])
            i += 1
        break
    elif f[int(a[i]) - 1] < int(a[i]):
        # Once we find a digit where f(x) is less than x, we stop
        break
    i += 1

# If we started replacing, we continue replacing until we find a digit that would be reduced
while i < n and f[int(a[i]) - 1] >= int(a[i]):
    max_number[i] = str(f[int(a[i]) - 1])
    i += 1

print(''.join(max_number))