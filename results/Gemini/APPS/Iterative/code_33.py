def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def solve():
    a1, b1, a2, b2, L, R = map(int, input().split())

    g = gcd(a1, a2)

    if (b2 - b1) % g != 0:
        print(0)
        return

    lcm = (a1 * a2) // g

    # Find the smallest x such that x = a1*k + b1 = a2*l + b2
    # a1*k + b1 = a2*l + b2
    # a1*k - a2*l = b2 - b1
    # a1*x - a2*y = gcd(a1, a2)
    # a1*(x * (b2-b1)/g) - a2*(y * (b2-b1)/g) = b2 - b1

    d, x, y = extended_gcd(a1, a2)
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g

    # General solution: k = x + (a2/g)*t, l = y + (a1/g)*t
    # x + (a2/g)*t >= 0
    # y + (a1/g)*t >= 0
    # k = x + (a2/g)*t
    # a1*(x + (a2/g)*t) + b1 >= L
    # a1*x + a1*(a2/g)*t + b1 >= L
    # t >= (L - a1*x - b1) / (a1*a2/g)
    # t >= (L - a1*x - b1) / lcm

    start_x = a1 * x + b1

    t_min = (L - start_x + lcm - 1) // lcm
    
    first_val = start_x + lcm * t_min

    if first_val > R:
        print(0)
        return
    
    count = (R - first_val) // lcm + 1

    print(count)

solve()