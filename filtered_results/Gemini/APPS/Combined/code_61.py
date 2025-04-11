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
        if f[a_list[i] - 1] < a_list[i]:
            end = i - 1
            break
    else:
        end = n - 1
        
    
    result = ""
    for i in range(n):
        if start <= i <= end:
            result += str(f[a_list[i] - 1])
        else:
            result += str(a_list[i])
            
    print(result)

solve()