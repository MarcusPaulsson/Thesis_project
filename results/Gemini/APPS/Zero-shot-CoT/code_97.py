def solve():
    s, c = input().split()
    n = len(s)

    if s < c:
        print(s)
        return
    
    best_s = None

    for i in range(n):
        for j in range(i + 1, n):
            temp_s = list(s)
            temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            temp_s = "".join(temp_s)
            
            if temp_s < c:
                if best_s is None or temp_s < best_s:
                    best_s = temp_s
    
    if best_s is not None:
        print(best_s)
    else:
        print("---")

t = int(input())
for _ in range(t):
    solve()