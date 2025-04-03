def solve():
    n = int(input())
    s = input()

    def calculate_operations(target):
        operations = 0
        i = 0
        while i < n:
            if s[i] != target[i % 2]:
                operations += 1
                j = i + 1
                while j < n and s[j] != target[i % 2]:
                    j += 1
                i = j
            else:
                i += 1
        return operations

    operations1 = calculate_operations("01")
    operations2 = calculate_operations("10")
    print(min(operations1, operations2))

t = int(input())
for _ in range(t):
    solve()