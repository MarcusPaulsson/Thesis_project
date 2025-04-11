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

    # Move examples to the front
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            # Find if the target position is already occupied by an example
            target_occupied_by_example = False
            for j in range(e):
                if examples[j][0] == str(i + 1):
                    target_occupied_by_example = True
                    break
            
            if target_occupied_by_example:
                # Find a temporary name
                temp_name = "temp"
                temp_idx = 0
                while True:
                    temp_name_with_idx = temp_name + str(temp_idx)
                    
                    name_exists = False
                    for k in range(n):
                        if files[k][0] == temp_name_with_idx:
                            name_exists = True
                            break
                    
                    if not name_exists:
                        break
                    
                    temp_idx += 1
                
                moves.append(f"move {examples[i][0]} {temp_name_with_idx}")
                
                # Find the file at the target position
                target_file = ""
                for k in range(n):
                    if files[k][0] == str(i + 1):
                        target_file = files[k][0]
                        break
                
                moves.append(f"move {target_file} {str(i + 1)}")
                moves.append(f"move {temp_name_with_idx} {str(i + 1)}")
                
                # Update the examples list
                for j in range(len(examples)):
                    if examples[j][0] == str(i + 1):
                        examples[j] = (str(i + 1), examples[j][1])
                        break
                examples[i] = (str(i + 1), examples[i][1])
            else:
                moves.append(f"move {examples[i][0]} {str(i + 1)}")
                examples[i] = (str(i + 1), examples[i][1])

    # Move regular tests to the back
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            
            # Find if the target position is already occupied by a regular test
            target_occupied_by_regular = False
            for j in range(len(regular)):
                if regular[j][0] == str(e + i + 1):
                    target_occupied_by_regular = True
                    break
            
            if target_occupied_by_regular:
                # Find a temporary name
                temp_name = "temp"
                temp_idx = 0
                while True:
                    temp_name_with_idx = temp_name + str(temp_idx)
                    
                    name_exists = False
                    for k in range(n):
                        if files[k][0] == temp_name_with_idx:
                            name_exists = True
                            break
                    
                    if not name_exists:
                        break
                    
                    temp_idx += 1
                
                moves.append(f"move {regular[i][0]} {temp_name_with_idx}")
                
                # Find the file at the target position
                target_file = ""
                for k in range(n):
                    if files[k][0] == str(e + i + 1):
                        target_file = files[k][0]
                        break
                
                moves.append(f"move {target_file} {str(e + i + 1)}")
                moves.append(f"move {temp_name_with_idx} {str(e + i + 1)}")
                
                # Update the regular list
                for j in range(len(regular)):
                    if regular[j][0] == str(e + i + 1):
                        regular[j] = (str(e + i + 1), regular[j][1])
                        break
                regular[i] = (str(e + i + 1), regular[i][1])
            else:
                moves.append(f"move {regular[i][0]} {str(e + i + 1)}")
                regular[i] = (str(e + i + 1), regular[i][1])

    print(len(moves))
    for move in moves:
        print(move)

solve()