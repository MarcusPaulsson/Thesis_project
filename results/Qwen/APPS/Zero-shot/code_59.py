def min_operations(n, x, y, number):
    target = '0' * y + '1' + '0' * (x - y - 1)
    operations = 0
    for i in range(n - x, n):
        if number[i] != target[i - (n - x)]:
            operations += 1
    return operations

n, x, y = map(int, input().split())
number = input()
print(min_operations(n, x, y, number))