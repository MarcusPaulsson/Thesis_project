def solve():
    n, k = map(int, input().split())
    s = list(input())

    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def find_operations(target):
        operations = []
        curr_s = list(s)

        def apply_operation(l, r):
            operations.append((l + 1, r + 1))
            curr_s[l:r+1] = curr_s[l:r+1][::-1]

        for i in range(n):
            if curr_s[i] != target[i]:
                for j in range(i + 1, n):
                    if curr_s[j] == target[i]:
                        apply_operation(i, j)
                        break
        return operations

    target = ['('] * k + [')'] * k + ['('] * (n // 2 - k) + [')'] * (n // 2 - k)
    
    operations = find_operations(target)

    print(len(operations))
    for l, r in operations:
        print(l, r)

t = int(input())
for _ in range(t):
    solve()