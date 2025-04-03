def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ops = []
    
    def get_mex(arr):
        s = set(arr)
        mex = 0
        while mex in s:
            mex += 1
        return mex

    for _ in range(2 * n):
        if all(a[i] <= a[i+1] for i in range(n-1)):
            break
        
        mex = get_mex(a)
        
        if mex < n:
            idx = -1
            for i in range(n):
                if a[i] == mex:
                    idx = i
                    break
            if idx != -1:
                a[idx] = mex
                ops.append(idx + 1)
            else:
                for i in range(n):
                    if a[i] != i:
                        a[i] = mex
                        ops.append(i+1)
                        break

        else:
            for i in range(n-1):
                if a[i] > a[i+1]:
                    a[i] = mex
                    ops.append(i+1)
                    break

    print(len(ops))
    print(*ops)

t = int(input())
for _ in range(t):
    solve()