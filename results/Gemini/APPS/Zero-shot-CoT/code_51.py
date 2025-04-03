def solve():
    n, k, d1, d2 = map(int, input().split())

    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            x = (k - s1 * d1 - s2 * d2) / 3
            if x < 0 or int(x) != x:
                continue
            
            w1 = x + s1 * d1
            w2 = x
            w3 = x + s2 * d2
            
            if w1 < 0 or w2 < 0 or w3 < 0:
                continue
            
            max_wins = max(w1, w2, w3)
            
            rem1 = max_wins - w1
            rem2 = max_wins - w2
            rem3 = max_wins - w3
            
            remaining_games = n // 3 * 3 - k
            
            if rem1 + rem2 + rem3 <= remaining_games and (remaining_games - (rem1 + rem2 + rem3)) % 3 == 0:
                if n % 3 == 0:
                  print("yes")
                  return
                else:
                  
                  print("no")
                  return

    print("no")

t = int(input())
for _ in range(t):
    solve()