def solve():
    n = int(input())
    a = list(map(int, input().split()))

    stack = []
    for x in a:
        if not stack:
            stack.append(x)
        elif stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    if not stack:
        print("YES")
    elif len(stack) == 1:
        print("YES")

    else:
        print("NO")

solve()