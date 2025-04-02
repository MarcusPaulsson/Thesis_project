def find_solution(d):
    if d == 0:
        return (0, 0)
    elif d < 2:
        return None
    else:
        for i in range(1, int(d/2)+1):
            a = i
            b = d - i
            if abs(a+b-a*b) <= 1e-6 and abs(a+b-d) <= 1e-6:
                return (a, b)
        return None

t = int(input())
for i in range(t):
    d = int(input())
    sol = find_solution(d)
    if sol is not None:
        print("Y {} {:.8f} {:.8f}".format(*sol))
    else:
        print("N")