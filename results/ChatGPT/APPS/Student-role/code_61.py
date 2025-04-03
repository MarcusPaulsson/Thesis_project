n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert the function f to a 1-indexed array
f = [0] + f

max_result = list(a)
started_replacement = False

for i in range(n):
    digit = int(a[i])
    if f[digit] > digit:
        if not started_replacement:
            started_replacement = True
        max_result[i] = str(f[digit])
    elif f[digit] < digit:
        if started_replacement:
            break

print(''.join(max_result))