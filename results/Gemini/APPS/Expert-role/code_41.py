def solve():
    n, k = map(int, input().split())
    s = list(input())

    def reverse(l, r):
        s[l-1:r] = s[l-1:r][::-1]

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

    def find_operations():
        operations = []
        
        # 1. Create the target string: "("*k + ")"*(k-1) + "()"*(n//2 - k)
        target = ['('] * k + [')'] * (k - 1) + ['(' , ')'] * (n//2 - k)
        
        # 2. Align the string with the target
        for i in range(n):
            if s[i] != target[i]:
                # Find the correct character in the remaining string
                for j in range(i + 1, n):
                    if s[j] == target[i]:
                        operations.append((i + 1, j + 1))
                        reverse(i + 1, j + 1)
                        break
        
        return operations

    operations = find_operations()

    print(len(operations))
    for l, r in operations:
        print(l, r)

t = int(input())
for _ in range(t):
    solve()