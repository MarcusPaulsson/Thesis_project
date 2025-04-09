def solve():
    a = int(input())
    
    if a == 1:
        print(1)
        return

    ans = 0
    power_of_2 = 1
    while power_of_2 < a:
        power_of_2 *= 2
        ans += 1
        
    print(ans)

solve()