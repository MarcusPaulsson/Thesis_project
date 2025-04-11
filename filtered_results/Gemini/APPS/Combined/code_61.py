def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    a_list = list(map(int, list(a)))
    
    start = -1
    end = -1
    
    for i in range(n):
        if f[a_list[i] - 1] > a_list[i] and start == -1:
            start = i
        if start != -1 and f[a_list[i] - 1] >= a_list[i]:
            end = i
        elif start != -1:
            break
            
    if start == -1:
        print(a)
    else:
        ans_list = a_list[:]
        for i in range(start, end + 1):
            ans_list[i] = f[a_list[i] - 1]
            
        print("".join(map(str, ans_list)))

solve()