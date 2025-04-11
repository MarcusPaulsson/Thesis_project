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
    
    e = len(examples)
    
    moves = []
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            # Find a temporary file name
            temp_name = None
            for j in range(1, n + 2):
                temp_name_str = str(j)
                
                is_used = False
                for k in range(n):
                    if files[k][0] == temp_name_str:
                        is_used = True
                        break
                if not is_used:
                    temp_name = temp_name_str
                    break
            
            if temp_name is None:
                print("Error: Could not find a temporary file name.")
                return
            
            # Move the example to the correct position
            if any(file[0] == str(i + 1) for file in files):
                moves.append(f"move {examples[i][0]} {temp_name}")
                
                # Find the file that is currently at the target position
                target_file = None
                for k in range(n):
                    if files[k][0] == str(i + 1):
                        target_file = files[k][0]
                        break
                
                moves.append(f"move {target_file} {str(i + 1)}")
                moves.append(f"move {temp_name} {examples[i][0]}")
                
                # Update the files list
                for k in range(n):
                    if files[k][0] == examples[i][0]:
                        files[k][0] = str(i + 1)
                    elif files[k][0] == target_file:
                        files[k][0] = examples[i][0]
                    elif files[k][0] == temp_name:
                        files[k][0] = target_file
            else:
                moves.append(f"move {examples[i][0]} {str(i + 1)}")
                
                # Update the files list
                for k in range(n):
                    if files[k][0] == examples[i][0]:
                        files[k][0] = str(i + 1)
                        break
    
    # Move regular tests to e + 1, e + 2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            
            # Find a temporary file name
            temp_name = None
            for j in range(1, n + 2):
                temp_name_str = str(j)
                
                is_used = False
                for k in range(n):
                    if files[k][0] == temp_name_str:
                        is_used = True
                        break
                if not is_used:
                    temp_name = temp_name_str
                    break
            
            if temp_name is None:
                print("Error: Could not find a temporary file name.")
                return
            
            # Move the regular test to the correct position
            if any(file[0] == str(e + i + 1) for file in files):
                moves.append(f"move {regular[i][0]} {temp_name}")
                
                # Find the file that is currently at the target position
                target_file = None
                for k in range(n):
                    if files[k][0] == str(e + i + 1):
                        target_file = files[k][0]
                        break
                
                moves.append(f"move {target_file} {str(e + i + 1)}")
                moves.append(f"move {temp_name} {regular[i][0]}")
                
                # Update the files list
                for k in range(n):
                    if files[k][0] == regular[i][0]:
                        files[k][0] = str(e + i + 1)
                    elif files[k][0] == target_file:
                        files[k][0] = regular[i][0]
                    elif files[k][0] == temp_name:
                        files[k][0] = target_file
            else:
                moves.append(f"move {regular[i][0]} {str(e + i + 1)}")
                
                # Update the files list
                for k in range(n):
                    if files[k][0] == regular[i][0]:
                        files[k][0] = str(e + i + 1)
                        break
    
    print(len(moves))
    for move in moves:
        print(move)

solve()