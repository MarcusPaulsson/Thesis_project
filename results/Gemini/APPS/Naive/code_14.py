def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    def is_stack_sortable(arr):
        stack = []
        b = []
        i = 0
        while i < len(arr) or stack:
            if stack and (i == len(arr) or stack[-1] < arr[i]):
                b.append(stack.pop())
            elif i < len(arr):
                stack.append(arr[i])
                i += 1
            else:
                return False
        
        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    remaining = sorted(list(set(range(1, n + 1)) - set(p)), reverse=True)
    
    permutation = p[:]
    
    for _ in range(n - k):
        permutation.append(remaining.pop(0))

    if is_stack_sortable(permutation):
        print(*permutation)
    else:
        print("-1")

solve()