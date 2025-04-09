def solve():
    n = int(input())
    s = input()
    t = input()

    def check(candidate):
        if s in candidate or t in candidate:
            return False
        return True

    base_patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]

    for pattern in base_patterns:
        candidate = pattern * n
        if check(candidate):
            print("YES")
            print(candidate)
            return

    
    alt_patterns = ["acbbac", "bacbac", "cabcab", "abcbca", "bcabac", "cbacba", "acbacb", "bacabc", "cbacab", "abcacb", "bcabca", "cabacb", "acbcba", "bacbca", "cbacab", "abcabc", "bcbcba", "cacbac"]
    
    if n == 2:
        for pattern in alt_patterns:
            if len(pattern) == 6 and check(pattern):
                print("YES")
                print(pattern)
                return
    
    if n == 3:
      alt_patterns_3 = ["cacbacbab", "abcabcabc", "acbacbacb", "bacbacbac"]
      for pattern in alt_patterns_3:
          if check(pattern):
              print("YES")
              print(pattern)
              return
    
    print("NO")

solve()