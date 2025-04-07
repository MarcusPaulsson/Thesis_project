def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))
    
    for start_kefa in range(l):
        temp_kefa = []
        for barrier in kefa:
            temp_kefa.append((barrier + start_kefa) % l)
        temp_kefa.sort()
        
        for start_sasha in range(l):
            temp_sasha = []
            for barrier in sasha:
                temp_sasha.append((barrier + start_sasha) % l)
            temp_sasha.sort()
            
            if temp_kefa == temp_sasha:
                print("YES")
                return
    
    print("NO")

solve()