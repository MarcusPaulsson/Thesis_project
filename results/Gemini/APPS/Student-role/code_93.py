def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    total_time = 0
    
    for i in range(m):
        present_to_send = b[i]
        
        index_in_stack = a.index(present_to_send)
        
        time_to_send = 2 * index_in_stack + 1
        total_time += time_to_send
        
        removed_presents = a[:index_in_stack]
        remaining_presents = a[index_in_stack+1:]
        
        a = removed_presents + remaining_presents

        
        reordered_removed_presents = []
        for j in range(len(removed_presents)):
            reordered_removed_presents.append(removed_presents[j])

        a = reordered_removed_presents + a
        
    print(total_time)

t = int(input())
for _ in range(t):
    solve()