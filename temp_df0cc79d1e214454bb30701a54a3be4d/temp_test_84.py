def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub_array = a[i:j+1]
            stack = []
            for element in sub_array:
                if not stack or stack[-1] != element:
                    stack.append(element)
                else:
                    stack.pop()
            if not stack:
                count += 1
    print(count)

q = int(input())
for _ in range(q):
    solve()