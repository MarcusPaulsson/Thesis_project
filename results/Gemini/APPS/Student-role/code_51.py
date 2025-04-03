def solve():
    n, k, d1, d2 = map(int, input().split())

    def check(x, y, z):
        if x < 0 or y < 0 or z < 0:
            return False
        if x + y + z > k:
            return False
        
        wins = n // 3
        
        rem_x = wins - x
        rem_y = wins - y
        rem_z = wins - z
        
        if rem_x < 0 or rem_y < 0 or rem_z < 0:
            return False
        
        if (rem_x + rem_y + rem_z) <= (n - k):
          if (n-k-rem_x-rem_y-rem_z) % 3 == 0:
            return True
          else:
            return False
        else:
          return False

    
    if n % 3 != 0:
      print("no")
      return
    
    if check(d1, d1 + d2, d2):
        print("yes")
        return
    
    if check(d1, d1 - d2, -d2):
        print("yes")
        return
    
    if check(-d1, -d1 + d2, d2 - d1):
        print("yes")
        return
    
    if check(-d1, -d1 - d2, -d2 - d1):
        print("yes")
        return
    
    print("no")

t = int(input())
for _ in range(t):
    solve()