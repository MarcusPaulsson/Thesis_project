def color_array(n, k, a):
    from collections import defaultdict

    color_assignment = [0] * n
    color_used = defaultdict(set)
    
    for i in range(n):
        num = a[i]
        for color in range(1, k + 1):
            if num not in color_used[color]:
                color_assignment[i] = color
                color_used[color].add(num)
                break
        else:
            print("NO")
            return

    if len(color_used) < k:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color_assignment)))

# Input reading
n, k = map(int, input().split())
a = list(map(int, input().split()))

color_array(n, k, a)