def construct_binary_string(a, b, x):
    if x == a + b - 1:
        return '0' * a + '1' * b
    elif x == 0:
        return '0' * a + '1' * b
    else:
        return '0' * (a - (x + 1) // 2) + '1' * (x + 1) + '0' * (a - (x + 1) // 2) + '1' * (b - x // 2)

a, b, x = map(int, input().split())
print(construct_binary_string(a, b, x))