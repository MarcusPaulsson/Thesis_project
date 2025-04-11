n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

max_number = list(a)
changed = False

for i in range(n):
    original_digit = int(a[i])
    mapped_digit = f[original_digit - 1]
    
    if mapped_digit > original_digit:
        if not changed:
            changed = True
            max_number[i] = str(mapped_digit)
        else:
            max_number[i] = str(mapped_digit)
    elif mapped_digit < original_digit and changed:
        break
    else:
        max_number[i] = str(original_digit)

print(''.join(max_number))