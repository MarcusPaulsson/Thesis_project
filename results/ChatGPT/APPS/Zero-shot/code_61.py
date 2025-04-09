n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Convert f to a list where the index represents the digit - 1
f = [0] + f  # f[0] is unused, we use indices 1 to 9

max_number = a  # Start with the original number

# We will look for the best segment to replace
changed = False
new_number = []

for i in range(n):
    digit = int(a[i])
    if f[digit] > digit:
        # Start replacing
        new_number.append(str(f[digit]))
        changed = True
    elif f[digit] < digit and changed:
        # Stop replacing if we already started
        break
    else:
        new_number.append(str(digit))

# If we started replacing but didn't stop, we should finalize it
if changed:
    max_number = ''.join(new_number) + a[i+1:]

# Output the maximum number
print(max(max_number, a))