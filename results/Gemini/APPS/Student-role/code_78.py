def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    
    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    def count_regular_sequences(n, s):
        count = 0
        
        def generate_sequences(current_seq, open_count, close_count):
            nonlocal count
            
            if len(current_seq) == 2 * n:
                if is_regular(current_seq) and s in current_seq:
                    count = (count + 1) % mod
                return
            
            if open_count < n:
                generate_sequences(current_seq + '(', open_count + 1, close_count)
            if close_count < open_count:
                generate_sequences(current_seq + ')', open_count, close_count + 1)
        
        generate_sequences("", 0, 0)
        return count
    
    print(count_regular_sequences(n, s))

solve()