n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

max_number = a
changed = False
start = 0

for i in range(n):
    current_digit = int(a[i])
    mapped_digit = f[current_digit - 1]
    
    if not changed and mapped_digit > current_digit:
        changed = True
        start = i
    elif changed and mapped_digit < current_digit:
        break

if changed:
    result = a[:start] + ''.join(str(f[int(d) - 1]) for d in a[start:i]) + a[i:]
    max_number = max(max_number, result)

print(max(max_number, a))