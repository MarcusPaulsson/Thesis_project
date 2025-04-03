n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

max_a = list(a)

# Flag to indicate if we are in the process of replacing
replacing = False

for i in range(n):
    original_digit = int(a[i])
    new_digit = f[original_digit - 1]
    
    if new_digit > original_digit:
        # Start replacing
        max_a[i] = str(new_digit)
        replacing = True
    elif new_digit < original_digit and replacing:
        # Stop replacing if we encounter a smaller digit
        break
    elif not replacing:
        max_a[i] = str(original_digit)

print(''.join(max_a))