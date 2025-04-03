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

    def count_regular_prefixes(seq):
        count = 0
        for i in range(1, len(seq) + 1):
            if is_regular(seq[:i]):
                count += 1
        return count

    def reverse_substring(l, r, seq):
        sub = seq[l-1:r]
        sub.reverse()
        seq[l-1:r] = sub

    operations = []

    # 1. Create the target string with k regular prefixes
    target = ['('] * k + [')'] * k + ['('] * (n // 2 - k) + [')'] * (n // 2 - k)
    
    # 2. Align the string
    for i in range(n):
        if s[i] != target[i]:
            # Find the correct element in the remaining string
            for j in range(i + 1, n):
                if s[j] == target[i]:
                    # Reverse the substring
                    operations.append((i + 1, j + 1))
                    reverse_substring(i + 1, j + 1, s)
                    break
    
    print(len(operations))
    for l, r in operations:
        print(l, r)

t = int(input())
for _ in range(t):
    solve()