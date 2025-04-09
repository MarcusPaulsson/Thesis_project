import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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
    
    d, x, y = extended_gcd(a1, a2)
    
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g

    x0 = x
    y0 = y
    
    x = x0 % (a2 // g)
    
    first_solution = a1 * x + b1
    
    k = math.ceil((L - first_solution) / lcm)
    
    first_valid = first_solution + k * lcm
    
    if first_valid > R:
        print(0)
        return
    
    k1 = math.ceil((-x0) / (a2 // g)) 
    
    x_pos = x0 + k1 * (a2 // g)

    first_solution_pos = a1 * x_pos + b1
    
    k_pos = math.ceil((L-first_solution_pos) / lcm)
    
    first_valid_pos = first_solution_pos + k_pos * lcm
    
    if first_valid_pos < L:
        k_pos +=1
        first_valid_pos = first_solution_pos + k_pos * lcm
        
    if first_valid_pos > R:
        print(0)
        return
    
    
    k2 = math.floor((R - first_valid_pos) / lcm)
    
    
    count = k2 + 1
    
    
    k_neg = math.floor((x0) / (a2 // g))
    
    x_neg = x0 - k_neg * (a2//g)
    
    first_solution_neg = a1 * x_neg + b1
    
    k_neg2 = math.ceil((L-first_solution_neg) / lcm)
    
    first_valid_neg = first_solution_neg + k_neg2 * lcm
    
    if first_valid_neg < L:
        k_neg2 += 1
        first_valid_neg = first_solution_neg + k_neg2 * lcm
        
    if first_valid_neg > R:
        print(0)
        return

    
    k_neg3 = math.floor((R - first_valid_neg) / lcm)
    
    
    count_neg = k_neg3+1
    
    
    if first_valid_pos == first_valid_neg:
        print(count)
    else:
        start = max(first_valid_pos, first_valid_neg)
        end = R
        
        k_total = math.floor((R - start) / lcm)
        
        print(k_total+1)

solve()