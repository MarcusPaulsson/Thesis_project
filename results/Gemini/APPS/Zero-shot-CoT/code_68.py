def solve():
    n = int(input())
    s = input()
    
    def calculate_operations(string):
        count = 0
        while string:
            max_ops = 0
            best_string = ""
            
            for i in range(len(string)):
                temp_string = string[:i] + string[i+1:]
                
                if temp_string:
                    first_char = temp_string[0]
                    prefix_len = 0
                    for j in range(len(temp_string)):
                        if temp_string[j] == first_char:
                            prefix_len += 1
                        else:
                            break
                    
                    new_string = temp_string[prefix_len:]
                else:
                    new_string = ""
                
                
                if len(string) > 0:
                  
                  if len(new_string) > len(best_string):
                    best_string = new_string
                    
                  elif len(new_string) == len(best_string) and len(best_string) > 0 :
                    if new_string < best_string:
                      best_string = new_string
                  elif len(best_string) == 0:
                      best_string = new_string

            string = best_string
            count += 1
        return count

    print(calculate_operations(s))


t = int(input())
for _ in range(t):
    solve()