a, b, x = map(int, input().split())

# Generate the base pattern
if x % 2 == 1:
    s = '01' * (x // 2) + '0' * (a - (x // 2 + 1)) + '1' * (b - (x // 2)) if a >= b else '10' * (x // 2) + '1' * (b - (x // 2 + 1)) + '0' * (a - (x // 2))
else:
    s = '01' * (x // 2) + '0' * (a - (x // 2)) + '1' * (b - (x // 2)) if a >= b else '10' * (x // 2) + '1' * (b - (x // 2)) + '0' * (a - (x // 2))

# Adjust the string to fit the counts of '0's and '1's
s = list(s)
zeros_needed = a - s.count('0')
ones_needed = b - s.count('1')

# Fill with remaining '0's and '1's
if zeros_needed > 0:
    for i in range(len(s)):
        if s[i] == '0' and zeros_needed > 0:
            continue
        if s[i] == '1' and ones_needed > 0:
            continue
        if zeros_needed > 0:
            s[i] = '0'
            zeros_needed -= 1
        elif ones_needed > 0:
            s[i] = '1'
            ones_needed -= 1

print(''.join(s))