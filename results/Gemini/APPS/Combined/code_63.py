def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    
    print(a[n-2] - a[0])

solve()