def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(l):
        possible = True
        shifted_kefa = [(x + start_diff) % l for x in kefa]
        shifted_kefa.sort()
        
        if shifted_kefa == sasha:
            print("YES")
            return
    
    print("NO")

solve()