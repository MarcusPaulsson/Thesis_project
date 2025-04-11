n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

max_number = list(a)
changed = False

for i in range(n):
    original_digit = int(a[i])
    new_digit = f[original_digit - 1]
    
    if new_digit > original_digit:
        if not changed:
            changed = True
            max_number[i] = str(new_digit)
        else:
            max_number[i] = str(new_digit)
    elif new_digit < original_digit and changed:
        break

print(''.join(max_number))