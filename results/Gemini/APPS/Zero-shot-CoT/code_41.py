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

    def find_substring(arr, start, target_char):
        for i in range(start, len(arr)):
            if arr[i] == target_char:
                return i
        return -1

    def reverse_substring(arr, l, r):
        arr[l-1:r] = arr[l-1:r][::-1]

    operations = []

    # Step 1: Create a regular sequence of (n/2) '(' followed by (n/2) ')'
    target = ['('] * (n // 2) + [')'] * (n // 2)
    
    for i in range(n):
        if s[i] != target[i]:
            idx = find_substring(s, i, target[i])
            reverse_substring(s, i+1, idx+1)
            operations.append((i+1, idx+1))
            
    # Step 2: Convert the first k-1 "()" into "((" and "))"
    for i in range(1, k):
        reverse_substring(s, 2*i, 2*i+1)
        operations.append((2*i, 2*i+1))

    print(len(operations))
    for l, r in operations:
        print(l, r)


t = int(input())
for _ in range(t):
    solve()