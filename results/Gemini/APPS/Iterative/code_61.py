def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    a_list = list(map(int, list(a)))
    
    start = -1
    end = -1
    
    for i in range(n):
        if f[a_list[i] - 1] > a_list[i]:
            start = i
            break
            
    if start == -1:
        print(a)
        return
    
    for i in range(start, n):
        if f[a_list[i] - 1] >= a_list[i]:
            end = i
        else:
            break
            
    
    for i in range(start, end + 1):
        a_list[i] = f[a_list[i] - 1]
        
    print("".join(map(str, a_list)))

solve()