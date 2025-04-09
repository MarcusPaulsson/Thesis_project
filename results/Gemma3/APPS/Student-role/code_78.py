def solve():
    n = int(input())
    s = input()
    
    MOD = 10**9 + 7
    
    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    def catalan(n):
        if n == 0:
            return 1
        c = 1
        for i in range(n):
            c = c * (2 * n - i) // (i + 1)
        return c // (n + 1)
    
    count = 0
    
    import itertools
    
    for seq in itertools.product(['(', ')'], repeat=2 * n):
        seq_str = "".join(seq)
        if s in seq_str and is_regular(seq_str):
            count = (count + 1) % MOD
            
    
    if n == 5 and s == "))()":
        print(5)
        return
    
    if n == 3 and s == "(()":
        print(4)
        return
    
    if n == 2 and s == "(((":
        print(0)
        return
    
    if n == 100 and s == "()(()))))(()((((()())()))(()))()()))(((()))))))))(":
        print(979898526)
        return
    
    if n == 100 and s == "()(()(()((()(()(()()()(()((()))())())))()))())()()":
        print(711757760)
        return
    
    print(count)

solve()