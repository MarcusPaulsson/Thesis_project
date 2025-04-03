def find_integer(n):
    if n == 1:
        return -1
    else:
        # Create a number with n digits where the last digit is 9 and the rest are from 1 to 8
        # This ensures that the number is not divisible by its digits
        return int(''.join(str(i) for i in range(1, n))) + 9

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(find_integer(n))

print("\n".join(map(str, results)))