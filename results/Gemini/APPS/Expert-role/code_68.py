def solve():
    n = int(input())
    s = input()
    
    def calculate_operations(string):
        operations = 0
        while string:
            operations += 1
            
            best_string = ""
            
            for i in range(len(string)):
                temp_string = list(string)
                del temp_string[i]
                temp_string = "".join(temp_string)
                
                if temp_string:
                    first_char = temp_string[0]
                    prefix_length = 0
                    for j in range(len(temp_string)):
                        if temp_string[j] == first_char:
                            prefix_length += 1
                        else:
                            break
                    temp_string = temp_string[prefix_length:]
                
                if not best_string or len(temp_string) > len(best_string):
                    best_string = temp_string
            
            string = best_string
        return operations
    
    print(calculate_operations(s))

t = int(input())
for _ in range(t):
    solve()