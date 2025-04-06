def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    stack = []
    
    for height in a:
        if not stack:
            stack.append(height)
        elif stack[-1] == height:
            stack.pop()
        else:
            stack.append(height)
            
    if not stack:
        print("YES")
    elif len(stack) == 1:
        print("YES")
    else:
        print("NO")

solve()