n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert f to a direct mapping for digits 0 to 9
f = [0] + f  # Add a dummy 0 at index 0 to make indexing easier

# Create the maximum number
max_number = list(a)
changed = False

for i in range(n):
    current_digit = int(a[i])
    if f[current_digit] > current_digit:
        max_number[i] = str(f[current_digit])
        changed = True  # Mark that we've started changing
    elif f[current_digit] < current_digit and changed:
        break  # Stop changing segment after we start

print("".join(max_number))