def solve():
  n = int(input())
  words = []
  for _ in range(n):
    words.append(input())

  def reverse_word(word):
    return word[::-1]

  def check(arr):
    for i in range(len(arr) - 1):
      if arr[i][-1] != arr[i+1][0]:
        return False
    return True

  def find_solution():
    for i in range(1 << n):
      reversed_indices = []
      temp_words = []
      for j in range(n):
        if (i >> j) & 1:
          reversed_indices.append(j + 1)
          temp_words.append(reverse_word(words[j]))
        else:
          temp_words.append(words[j])

      
      if len(set(temp_words)) != n:
        continue
      
      import itertools
      for perm in itertools.permutations(temp_words):
          if check(list(perm)):
              return len(reversed_indices), reversed_indices

    return -1, []

  k, reversed_indices = find_solution()
  
  if k == -1:
    print(-1)
  else:
    print(k)
    if k > 0:
      print(*reversed_indices)
    

t = int(input())
for _ in range(t):
  solve()