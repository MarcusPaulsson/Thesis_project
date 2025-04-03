def find_integer(n):
    if n == 1:
        return -1
    else:
        # Create a number by using digits from 1 to 9
        # We can use the digits 2 to 9 to ensure no digit is 0
        return ''.join(str((i % 9) + 1) for i in range(n))

t = int(input())
for _ in range(t):
    n = int(input())
    print(find_integer(n))