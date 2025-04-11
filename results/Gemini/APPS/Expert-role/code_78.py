def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)

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

    def contains_substring(seq, sub):
        return sub in seq

    count = 0
    
    def generate_sequences(current_seq, open_count, close_count):
        nonlocal count
        if len(current_seq) == 2 * n:
            if is_regular(current_seq) and contains_substring(current_seq, s):
                count = (count + 1) % mod
            return

        if open_count < n:
            generate_sequences(current_seq + '(', open_count + 1, close_count)
        if close_count < open_count:
            generate_sequences(current_seq + ')', open_count, close_count + 1)

    generate_sequences("", 0, 0)
    print(count)

solve()