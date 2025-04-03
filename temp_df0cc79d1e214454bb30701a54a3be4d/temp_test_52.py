def solve():
    n, k, d1, d2 = map(int, input().split())
    
    def check(x, y, z):
        if x < 0 or y < 0 or z < 0:
            return False
        if x + y + z > k:
            return False
        
        mx = max(x, y, z)
        rem = n // 3 * 3 - (x + y + z)
        if rem < 0:
            return False
        
        if rem % 3 != 0:
            return False
            
        need = mx * 3 - (x+y+z)
        
        if need > n-k:
            return False
        
        if (n-k-need)%3 !=0:
            return False
            
        return True

    for sgn1 in [-1, 1]:
        for sgn2 in [-1, 1]:
            x = (d1 * sgn1 - d2 * sgn2)
            if x % 3 != 0:
                continue
            x //= 3
            y = x + d2 * sgn2
            z = y - d1 * sgn1
            
            if check(x, y, z):
                print("yes")
                return

    print("no")

t = int(input())
for _ in range(t):
    solve()