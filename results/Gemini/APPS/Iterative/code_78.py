def solve():
    n = int(input())
    s = input()
    len_s = len(s)
    mod = 10**9 + 7

    dp = {}

    def count_regular_sequences(length, balance, contains_s):
        if length == 2 * n:
            if balance == 0 and contains_s:
                return 1
            else:
                return 0

        if (length, balance, contains_s) in dp:
            return dp[(length, balance, contains_s)]

        count = 0
        
        # Add '('
        if balance + 1 <= n:
            new_contains_s = contains_s
            temp_seq = ""
            if length < len_s:
                temp_seq = '(' + s[length+1:] if length + 1 < len_s else '('
                if len(temp_seq) > 0 and s[:length+1] == temp_seq[:length+1]:
                  new_contains_s = True
            else:
              
                new_contains_s = contains_s
            
            
            seq = ('(' + s[length+1:]) if length + 1 < len_s else '('
            if not contains_s and len_s <= 2 * n and length < len_s and len(seq) > 0 and s.startswith(seq):
                new_contains_s = True

            count = (count + count_regular_sequences(length + 1, balance + 1, new_contains_s)) % mod
        
        # Add ')'
        if balance > 0:
            new_contains_s = contains_s
            temp_seq = ""
            if length < len_s:
                temp_seq = ')' + s[length+1:]  if length + 1 < len_s else ')'
                if len(temp_seq) > 0 and s[:length+1] == temp_seq[:length+1]:
                  new_contains_s = True
            else:
                new_contains_s = contains_s

            seq = (')' + s[length+1:]) if length + 1 < len_s else ')'
            if not contains_s and len_s <= 2 * n and length < len_s and len(seq) > 0 and s.startswith(seq):
                new_contains_s = True
            
            count = (count + count_regular_sequences(length + 1, balance - 1, new_contains_s)) % mod

        dp[(length, balance, contains_s)] = count
        return count

    contains_s = False
    if len_s == 0:
      contains_s = True
    
    print(count_regular_sequences(0, 0, False))

solve()