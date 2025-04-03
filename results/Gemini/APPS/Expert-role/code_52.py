def solve():
    n, k, d1, d2 = map(int, input().split())

    def check(x, y, z):
        if x < 0 or y < 0 or z < 0:
            return False
        if x + y + z > k:
            return False
        
        mx = max(x, y, z)
        rem = n // 3 * 3 - k

        if rem < 0:
            return False
        
        if (rem % 3 != 0):
          return False

        if mx * 3 > n:
          return False
          
        
        return True

    possible = False
    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            x = (d1 * s1 + d2 * s1 * s2)
            if x % 3 != 0:
                continue
            x //= 3
            y = d1 * s1 + x
            z = d2 * s2 + y
            
            if check(x, y, z):
                possible = True
                break
        if possible:
            break
    
    if possible:
        print("yes")
    else:
        print("no")

t = int(input())
for _ in range(t):
    solve()