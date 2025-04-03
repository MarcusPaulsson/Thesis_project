def solve():
    t = int(input())
    x = list(map(int, input().split()))

    for target in x:
        if target < 19:
            if target == 5 or target == 6 or target == 7 or target == 8 or target == 9 or target == 10 or target == 11 or target == 12 or target == 13 or target == 14 or target == 15 or target == 16 or target == 17 or target == 18:
              print("YES")
            elif target == 1:
              print("YES")
            elif target == 2:
              print("YES")
            elif target == 3:
              print("YES")
            elif target == 4:
              print("YES")
            elif target == 19:
              print("YES")
            
            else:
              print("NO")
            
        else:
            print("YES")

solve()