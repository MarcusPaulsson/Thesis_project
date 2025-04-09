def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(n):
        temp = []
        for i in range(n):
            temp.append((sasha[i] + kefa[0]) % l)
        
        temp.sort()
        
        kefa_shifted = []
        for i in range(n):
          kefa_shifted.append((kefa[i] + 0) % l)
        kefa_shifted.sort()

        if temp == kefa_shifted:
          print("YES")
          return
          
        sasha = sasha[1:] + [sasha[0]]
        
    print("NO")

solve()