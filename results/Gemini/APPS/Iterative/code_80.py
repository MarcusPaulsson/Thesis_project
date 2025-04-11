def solve():
    n = int(input())
    s = input()
    
    colors = [0] * n
    
    tails = []
    
    for i in range(n):
        found = False
        for j in range(len(tails)):
            if s[i] >= tails[j]:
                tails[j] = s[i]
                colors[i] = j + 1
                found = True
                break
        if not found:
            tails.append(s[i])
            colors[i] = len(tails)
            
    print(len(tails))
    print(*colors)

solve()