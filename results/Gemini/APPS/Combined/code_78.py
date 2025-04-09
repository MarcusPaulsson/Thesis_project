def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    len_s = len(s)

    dp = {}

    def count_regular_sequences(length, balance, has_substring):
        if length == 0:
            if balance == 0 and has_substring:
                return 1
            else:
                return 0

        if (length, balance, has_substring) in dp:
            return dp[(length, balance, has_substring)]

        count = 0
        
        # Add '('
        if balance + 1 <= n:
            new_has_substring = has_substring
            if not has_substring:
                temp_seq = "("
                if len_s > 1:
                  temp_seq = s[:1]
                
                if temp_seq == s[:1]:
                    
                    count = (count + count_regular_sequences(length - 1, balance + 1, s[:1] == s)) % mod
                else:
                    count = (count + count_regular_sequences(length - 1, balance + 1, False)) % mod
            else:
                 count = (count + count_regular_sequences(length - 1, balance + 1, True)) % mod
        
        # Add ')'
        if balance > 0:
            new_has_substring = has_substring
            if not has_substring:
                temp_seq = ")"
                if len_s > 1:
                  temp_seq = s[:1]
                if temp_seq == s[:1]:
                   
                    count = (count + count_regular_sequences(length - 1, balance - 1, s[:1] == s)) % mod
                else:
                     count = (count + count_regular_sequences(length - 1, balance - 1, False)) % mod
            else:
                count = (count + count_regular_sequences(length - 1, balance - 1, True)) % mod

        dp[(length, balance, has_substring)] = count
        return count

    def count_regular_sequences_with_substring(n, s):
      
      
      def kmp_table(w):
          T = [0] * len(w)
          pos = 1
          cnd = 0
          while pos < len(w):
              if w[pos] == w[cnd]:
                  T[pos] = cnd + 1
                  pos += 1
                  cnd += 1
              elif cnd > 0:
                  cnd = T[cnd-1]
              else:
                  pos += 1
          return T
      
      def count_regular_sequences_dp(length, balance, kmp_state):
          if length == 0:
              if balance == 0:
                  return 1
              else:
                  return 0
          
          if (length, balance, kmp_state) in dp:
              return dp[(length, balance, kmp_state)]
          
          count = 0
          
          # Add '('
          if balance + 1 <= n:
              new_kmp_state = kmp_state
              while new_kmp_state > 0 and s[new_kmp_state] != '(':
                  new_kmp_state = table[new_kmp_state - 1]
              if s[new_kmp_state] == '(':
                  new_kmp_state += 1
              
              count = (count + count_regular_sequences_dp(length - 1, balance + 1, new_kmp_state)) % mod
          
          # Add ')'
          if balance > 0:
              new_kmp_state = kmp_state
              while new_kmp_state > 0 and s[new_kmp_state] != ')':
                  new_kmp_state = table[new_kmp_state - 1]
              if s[new_kmp_state] == ')':
                  new_kmp_state += 1
              
              count = (count + count_regular_sequences_dp(length - 1, balance - 1, new_kmp_state)) % mod
          
          dp[(length, balance, kmp_state)] = count
          return count
      
      table = kmp_table(s)
      dp.clear()
      
      total_regular_sequences = count_regular_sequences_dp(2 * n, 0, 0)
      dp.clear()
      
      def count_regular_sequences_dp_no_substring(length, balance, kmp_state):
          if length == 0:
              if balance == 0:
                  return 1
              else:
                  return 0
          
          if (length, balance, kmp_state) in dp:
              return dp[(length, balance, kmp_state)]
          
          count = 0
          
          # Add '('
          if balance + 1 <= n:
              new_kmp_state = kmp_state
              while new_kmp_state > 0 and s[new_kmp_state] != '(':
                  new_kmp_state = table[new_kmp_state - 1]
              if s[new_kmp_state] == '(':
                  new_kmp_state += 1
              
              if new_kmp_state != len_s:
                count = (count + count_regular_sequences_dp_no_substring(length - 1, balance + 1, new_kmp_state)) % mod
          
          # Add ')'
          if balance > 0:
              new_kmp_state = kmp_state
              while new_kmp_state > 0 and s[new_kmp_state] != ')':
                  new_kmp_state = table[new_kmp_state - 1]
              if s[new_kmp_state] == ')':
                  new_kmp_state += 1
              
              if new_kmp_state != len_s:
                count = (count + count_regular_sequences_dp_no_substring(length - 1, balance - 1, new_kmp_state)) % mod
          
          dp[(length, balance, kmp_state)] = count
          return count
      
      
      
      table = kmp_table(s)
      dp.clear()
      
      total_regular_sequences_without_substring = count_regular_sequences_dp_no_substring(2 * n, 0, 0)
      
      return (total_regular_sequences - total_regular_sequences_without_substring) % mod

    
    
    print(count_regular_sequences_with_substring(n, s))

solve()