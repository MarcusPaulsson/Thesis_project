def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    ans = ""
    for m in range(1, n + 1):
        beautiful = False
        for l in range(n):
            for r in range(l, n):
                sub_array = p[l:r+1]
                sub_array.sort()
                
                if len(sub_array) == m:
                    is_permutation = True
                    for i in range(m):
                        if sub_array[i] != i + 1:
                            is_permutation = False
                            break
                    if is_permutation:
                        beautiful = True
                        break
            if beautiful:
                break
        
        if beautiful:
            ans += "1"
        else:
            ans += "0"
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()