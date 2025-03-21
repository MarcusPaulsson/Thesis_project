def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    result = ""
    for m in range(1, n + 1):
        is_beautiful = False
        for l in range(n):
            for r in range(l, n):
                sub_array = p[l:r+1]
                if len(sub_array) == m:
                    nums = sorted(sub_array)
                    if nums == list(range(1, m + 1)):
                        is_beautiful = True
                        break
            if is_beautiful:
                break
        result += "1" if is_beautiful else "0"
    print(result)

t = int(input())
for _ in range(t):
    solve()