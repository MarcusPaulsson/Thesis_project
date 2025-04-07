n = int(input())
a = input().strip()
f = list(map(int, input().split()))

max_number = list(a)
changed = False

for i in range(n):
    current_digit = int(a[i])
    new_digit = f[current_digit - 1]
    
    if new_digit > current_digit:
        if not changed:
            changed = True
        max_number[i] = str(new_digit)
    elif new_digit < current_digit and changed:
        break

print(''.join(max_number))