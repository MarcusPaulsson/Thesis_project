n = int(input())
a = input().strip()
f = list(map(int, input().split()))

result = list(a)
changed = False

for i in range(n):
    original_digit = int(a[i])
    new_digit = f[original_digit - 1]
    
    if new_digit > original_digit:
        result[i] = str(new_digit)
        changed = True
    elif new_digit < original_digit and changed:
        break

print(''.join(result))