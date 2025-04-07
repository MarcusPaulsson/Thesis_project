def f(x):
    x += 1
    while x % 10 == 0 and x > 0:
        x //= 10
    return x

def reachable(n):
    reachable_numbers = set()
    q = [n]
    reachable_numbers.add(n)
    
    while q:
        curr = q.pop(0)
        next_num = f(curr)
        if next_num not in reachable_numbers and next_num <= 10**9:
            reachable_numbers.add(next_num)
            q.append(next_num)
    
    return len(reachable_numbers)

if __name__ == "__main__":
    n = int(input())
    print(reachable(n))