def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())

    examples = []
    regular = []
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))

    moves = []
    
    e = len(examples)
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            if any(files[j][0] == str(i+1) for j in range(n)):
                # Need to swap
                
                # Find a temporary name
                temp_name = "temp"
                temp_count = 0
                while any(files[j][0] == temp_name for j in range(n)):
                    temp_count += 1
                    temp_name = "temp" + str(temp_count)
                
                moves.append(f"move {examples[i][0]} {temp_name}")
                
                # Find the file that is currently named i+1
                current_name_at_target = ""
                for j in range(n):
                    if files[j][0] == str(i+1):
                        current_name_at_target = files[j][0]
                        break
                
                moves.append(f"move {current_name_at_target} {examples[i][0]}")
                moves.append(f"move {temp_name} {str(i+1)}")
                
            else:
                moves.append(f"move {examples[i][0]} {str(i + 1)}")
            
    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            
            if any(files[j][0] == str(e+i+1) for j in range(n)):
                # Need to swap
                
                # Find a temporary name
                temp_name = "temp"
                temp_count = 0
                while any(files[j][0] == temp_name for j in range(n)):
                    temp_count += 1
                    temp_name = "temp" + str(temp_count)
                
                moves.append(f"move {regular[i][0]} {temp_name}")
                
                # Find the file that is currently named e+i+1
                current_name_at_target = ""
                for j in range(n):
                    if files[j][0] == str(e+i+1):
                        current_name_at_target = files[j][0]
                        break
                
                moves.append(f"move {current_name_at_target} {regular[i][0]}")
                moves.append(f"move {temp_name} {str(e+i+1)}")
                
            else:
                moves.append(f"move {regular[i][0]} {str(e + i + 1)}")

    print(len(moves))
    for move in moves:
        print(move)

solve()